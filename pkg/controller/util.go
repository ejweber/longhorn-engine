package controller

import (
	"fmt"

	"github.com/pkg/errors"

	"github.com/longhorn/longhorn-engine/pkg/replica/client"
	"github.com/longhorn/longhorn-engine/pkg/types"
)

func GetReplicaDisksAndHead(address string) (map[string]types.DiskInfo, string, error) {
	// TODO: How can we know volume name here?
	repClient, err := client.NewReplicaClient(address, "")
	if err != nil {
		return nil, "", errors.Wrapf(err, "cannot get replica client for %v", address)
	}
	defer repClient.Close()

	rep, err := repClient.GetReplica()
	if err != nil {
		return nil, "", errors.Wrapf(err, "cannot get replica for %v", address)
	}

	if len(rep.Chain) == 0 {
		return nil, "", fmt.Errorf("replica on %v does not have any non-removed disks", address)
	}

	disks := map[string]types.DiskInfo{}
	head := rep.Chain[0]
	for diskName, info := range rep.Disks {
		// skip volume head
		if diskName == head {
			continue
		}
		// skip backing file
		if diskName == rep.BackingFile {
			continue
		}
		disks[diskName] = info
	}
	return disks, head, nil
}
