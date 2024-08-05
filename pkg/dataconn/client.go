package dataconn

import (
	"errors"
	"io"
	"net"
	"sync/atomic"
	"time"

	"github.com/sirupsen/logrus"

	journal "github.com/longhorn/sparse-tools/stats"
)

var (
	//ErrRWTimeout r/w operation timeout
	ErrRWTimeout = errors.New("r/w timeout")
)

// Client replica client
type Client struct {
	end       chan struct{}
	requests  chan *Message
	send      chan *Message
	responses chan *Message
	seq       uint32
	messages  map[uint32]*Message
	wires     []*Wire
	peerAddr  string

	// The dataconn client tracks the amount of time since the last successful I/O operation, but it is up to the upper
	// layer to determine whether a timeoutChan has occured as a result. This sharing of responsibilty allows:
	// - The dataconn client to handle its own in-flight I/O, and
	// - The upper layer to dynamically decide on an "acceptable" timeoutChan (based on the status of the other
	//   available replicas.)
	timeoutChan           chan struct{}
	durationSinceResponse *atomic.Int64
}

// NewClient replica client
func NewClient(conns []net.Conn, engineToReplicaTimeout time.Duration) *Client {
	var wires []*Wire
	for _, conn := range conns {
		wires = append(wires, NewWire(conn))
	}
	c := &Client{
		wires:     wires,
		peerAddr:  conns[0].RemoteAddr().String(),
		end:       make(chan struct{}, 1024),
		requests:  make(chan *Message, 1024),
		send:      make(chan *Message, 1024),
		responses: make(chan *Message, 1024),
		messages:  map[uint32]*Message{},

		timeoutChan:           make(chan struct{}),
		durationSinceResponse: &atomic.Int64{},
	}
	go c.loop()
	c.write()
	c.read()
	return c
}

// TargetID operation target ID
func (c *Client) TargetID() string {
	return c.peerAddr
}

// WriteAt replica client
func (c *Client) WriteAt(buf []byte, offset int64) (int, error) {
	return c.operation(TypeWrite, buf, uint32(len(buf)), offset)
}

// UnmapAt replica client
func (c *Client) UnmapAt(length uint32, offset int64) (int, error) {
	return c.operation(TypeUnmap, nil, length, offset)
}

// SetError replica client transport error
func (c *Client) SetError(err error) {
	c.responses <- &Message{
		transportErr: err,
	}
}

// ReadAt replica client
func (c *Client) ReadAt(buf []byte, offset int64) (int, error) {
	return c.operation(TypeRead, buf, uint32(len(buf)), offset)
}

// Ping replica client
func (c *Client) Ping() error {
	_, err := c.operation(TypePing, nil, 0, 0)
	return err
}

func (c *Client) operation(op uint32, buf []byte, length uint32, offset int64) (int, error) {
	msg := Message{
		Complete: make(chan struct{}, 1),
		Type:     op,
		Offset:   offset,
		Size:     length,
		Data:     nil,
	}

	if op == TypeWrite {
		msg.Data = buf
	}

	c.requests <- &msg

	<-msg.Complete
	// Only copy the message if a read is requested
	if op == TypeRead && (msg.Type == TypeResponse || msg.Type == TypeEOF) {
		copy(buf, msg.Data)
	}
	if msg.Type == TypeError {
		return 0, errors.New(string(msg.Data))
	}
	if msg.Type == TypeEOF {
		return int(msg.Size), io.EOF
	}
	return int(msg.Size), nil
}

// Close replica client
func (c *Client) Close() {
	for _, wire := range c.wires {
		wire.Close()
	}
	c.end <- struct{}{}
}

func (c *Client) GetTimeoutChannel() chan struct{} {
	return c.timeoutChan
}

// GetDurationSinceResponseShared returns and atomic.Int64. Other goroutines can access it safely using atomic
// operations, but it must be cast to a time.Duration before duration operations can be used.
func (c *Client) GetDurationSinceResponseShared() *atomic.Int64 {
	return c.durationSinceResponse
}

func (c *Client) loop() {
	defer close(c.send)

	var clientError error
	var ioInflight int

	// handleClientError cleans up all in flight messages
	// also stores the error so that future requests/responses get errored immediately.
	handleClientError := func(err error) {
		clientError = err
		for _, msg := range c.messages {
			c.replyError(msg, err)
		}

		ioInflight = 0
		c.durationSinceResponse.Store(-1)
	}

	for {
		select {
		case <-c.end:
			return
		case <-c.timeoutChan:
			logrus.Errorf("R/W Timeout. No response received in %v", time.Duration(c.durationSinceResponse.Load()))
			handleClientError(ErrRWTimeout)
			journal.PrintLimited(1000)
		case req := <-c.requests:
			if clientError != nil {
				c.replyError(req, clientError)
				continue
			}

			if req.Type == TypeRead || req.Type == TypeWrite || req.Type == TypeUnmap {
				if ioInflight == 0 {
					// >= 0 means we are waiting on an I/O operation to complete.
					c.durationSinceResponse.Store(0)
				}
				ioInflight++
			}

			c.handleRequest(req)
		case resp := <-c.responses:
			if resp.transportErr != nil {
				handleClientError(resp.transportErr)
				continue
			}

			req, pending := c.messages[resp.Seq]
			if !pending {
				logrus.Warnf("Received response message id %v seq %v type %v for non pending request", resp.ID, resp.Seq, resp.Type)
				continue
			}

			if req.Type == TypeRead || req.Type == TypeWrite || req.Type == TypeUnmap {
				ioInflight--
				if ioInflight > 0 {
					// >= 0 means we are waiting on an I/O operation to complete.
					c.durationSinceResponse.Store(0)
				} else if ioInflight == 0 {
					// < 0 means we are not waiting on an I/O operation to complete.
					c.durationSinceResponse.Store(-1)
				}
			}

			if clientError != nil {
				c.replyError(req, clientError)
				continue
			}

			c.handleResponse(resp)
		}
	}
}

func (c *Client) nextSeq() uint32 {
	c.seq++
	return c.seq
}

func (c *Client) replyError(req *Message, err error) {
	if opErr := journal.RemovePendingOp(req.ID, false); opErr != nil {
		logrus.WithError(opErr).WithFields(logrus.Fields{
			"seq": req.Seq,
			"id":  req.ID,
		}).Warn("Error removing pending operation")
	}
	delete(c.messages, req.Seq)
	req.Type = TypeError
	req.Data = []byte(err.Error())
	req.Complete <- struct{}{}
}

func (c *Client) handleRequest(req *Message) {
	switch req.Type {
	case TypeRead:
		req.ID = journal.InsertPendingOp(time.Now(), c.TargetID(), journal.OpRead, int(req.Size))
	case TypeWrite:
		req.ID = journal.InsertPendingOp(time.Now(), c.TargetID(), journal.OpWrite, int(req.Size))
	case TypeUnmap:
		req.ID = journal.InsertPendingOp(time.Now(), c.TargetID(), journal.OpUnmap, int(req.Size))
	case TypePing:
		req.ID = journal.InsertPendingOp(time.Now(), c.TargetID(), journal.OpPing, 0)
	}

	req.MagicVersion = MagicVersion
	req.Seq = c.nextSeq()
	c.messages[req.Seq] = req
	c.send <- req
}

func (c *Client) handleResponse(resp *Message) {
	if req, ok := c.messages[resp.Seq]; ok {
		err := journal.RemovePendingOp(req.ID, true)
		if err != nil {
			logrus.WithError(err).WithFields(logrus.Fields{
				"seq": resp.Seq,
				"id":  req.ID,
			}).Warn("Error removing pending operation")
		}
		delete(c.messages, resp.Seq)
		req.Type = resp.Type
		req.Size = resp.Size
		req.Data = resp.Data
		req.Complete <- struct{}{}
	}
}

func (c *Client) write() {
	for _, wire := range c.wires {
		go func(w *Wire) {
			for msg := range c.send {
				if err := w.Write(msg); err != nil {
					c.responses <- &Message{
						transportErr: err,
					}
				}
			}
		}(wire)
	}
}

func (c *Client) read() {
	for _, wire := range c.wires {
		go func(w *Wire) {
			for {
				msg, err := w.Read()
				if err != nil {
					logrus.WithError(err).Errorf("Error reading from wire %v", c.peerAddr)
					c.responses <- &Message{
						transportErr: err,
					}
					break
				}
				c.responses <- msg
			}
		}(wire)
	}
}
