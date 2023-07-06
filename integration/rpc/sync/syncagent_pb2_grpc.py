# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import syncagent_pb2 as syncagent__pb2


class SyncAgentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FileRemove = channel.unary_unary(
        '/ptypes.SyncAgentService/FileRemove',
        request_serializer=syncagent__pb2.FileRemoveRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FileRename = channel.unary_unary(
        '/ptypes.SyncAgentService/FileRename',
        request_serializer=syncagent__pb2.FileRenameRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FileSend = channel.unary_unary(
        '/ptypes.SyncAgentService/FileSend',
        request_serializer=syncagent__pb2.FileSendRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.FilesSync = channel.unary_unary(
        '/ptypes.SyncAgentService/FilesSync',
        request_serializer=syncagent__pb2.FilesSyncRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotClone = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotClone',
        request_serializer=syncagent__pb2.SnapshotCloneRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.VolumeExport = channel.unary_unary(
        '/ptypes.SyncAgentService/VolumeExport',
        request_serializer=syncagent__pb2.VolumeExportRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ReceiverLaunch = channel.unary_unary(
        '/ptypes.SyncAgentService/ReceiverLaunch',
        request_serializer=syncagent__pb2.ReceiverLaunchRequest.SerializeToString,
        response_deserializer=syncagent__pb2.ReceiverLaunchResponse.FromString,
        )
    self.BackupCreate = channel.unary_unary(
        '/ptypes.SyncAgentService/BackupCreate',
        request_serializer=syncagent__pb2.BackupCreateRequest.SerializeToString,
        response_deserializer=syncagent__pb2.BackupCreateResponse.FromString,
        )
    self.BackupRemove = channel.unary_unary(
        '/ptypes.SyncAgentService/BackupRemove',
        request_serializer=syncagent__pb2.BackupRemoveRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BackupRestore = channel.unary_unary(
        '/ptypes.SyncAgentService/BackupRestore',
        request_serializer=syncagent__pb2.BackupRestoreRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.BackupStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/BackupStatus',
        request_serializer=syncagent__pb2.BackupStatusRequest.SerializeToString,
        response_deserializer=syncagent__pb2.BackupStatusResponse.FromString,
        )
    self.Reset = channel.unary_unary(
        '/ptypes.SyncAgentService/Reset',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.RestoreStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/RestoreStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syncagent__pb2.RestoreStatusResponse.FromString,
        )
    self.SnapshotPurge = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotPurge',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotPurgeStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotPurgeStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syncagent__pb2.SnapshotPurgeStatusResponse.FromString,
        )
    self.ReplicaRebuildStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/ReplicaRebuildStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syncagent__pb2.ReplicaRebuildStatusResponse.FromString,
        )
    self.SnapshotCloneStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotCloneStatus',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syncagent__pb2.SnapshotCloneStatusResponse.FromString,
        )
    self.SnapshotHash = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotHash',
        request_serializer=syncagent__pb2.SnapshotHashRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotHashStatus = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotHashStatus',
        request_serializer=syncagent__pb2.SnapshotHashStatusRequest.SerializeToString,
        response_deserializer=syncagent__pb2.SnapshotHashStatusResponse.FromString,
        )
    self.SnapshotHashCancel = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotHashCancel',
        request_serializer=syncagent__pb2.SnapshotHashCancelRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SnapshotHashLockState = channel.unary_unary(
        '/ptypes.SyncAgentService/SnapshotHashLockState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=syncagent__pb2.SnapshotHashLockStateResponse.FromString,
        )


class SyncAgentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FileRemove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileRename(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileSend(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FilesSync(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotClone(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VolumeExport(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiverLaunch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupRemove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupRestore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BackupStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Reset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestoreStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotPurge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotPurgeStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicaRebuildStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotCloneStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHashStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHashCancel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SnapshotHashLockState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SyncAgentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FileRemove': grpc.unary_unary_rpc_method_handler(
          servicer.FileRemove,
          request_deserializer=syncagent__pb2.FileRemoveRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FileRename': grpc.unary_unary_rpc_method_handler(
          servicer.FileRename,
          request_deserializer=syncagent__pb2.FileRenameRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FileSend': grpc.unary_unary_rpc_method_handler(
          servicer.FileSend,
          request_deserializer=syncagent__pb2.FileSendRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'FilesSync': grpc.unary_unary_rpc_method_handler(
          servicer.FilesSync,
          request_deserializer=syncagent__pb2.FilesSyncRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotClone': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotClone,
          request_deserializer=syncagent__pb2.SnapshotCloneRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'VolumeExport': grpc.unary_unary_rpc_method_handler(
          servicer.VolumeExport,
          request_deserializer=syncagent__pb2.VolumeExportRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ReceiverLaunch': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiverLaunch,
          request_deserializer=syncagent__pb2.ReceiverLaunchRequest.FromString,
          response_serializer=syncagent__pb2.ReceiverLaunchResponse.SerializeToString,
      ),
      'BackupCreate': grpc.unary_unary_rpc_method_handler(
          servicer.BackupCreate,
          request_deserializer=syncagent__pb2.BackupCreateRequest.FromString,
          response_serializer=syncagent__pb2.BackupCreateResponse.SerializeToString,
      ),
      'BackupRemove': grpc.unary_unary_rpc_method_handler(
          servicer.BackupRemove,
          request_deserializer=syncagent__pb2.BackupRemoveRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BackupRestore': grpc.unary_unary_rpc_method_handler(
          servicer.BackupRestore,
          request_deserializer=syncagent__pb2.BackupRestoreRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'BackupStatus': grpc.unary_unary_rpc_method_handler(
          servicer.BackupStatus,
          request_deserializer=syncagent__pb2.BackupStatusRequest.FromString,
          response_serializer=syncagent__pb2.BackupStatusResponse.SerializeToString,
      ),
      'Reset': grpc.unary_unary_rpc_method_handler(
          servicer.Reset,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'RestoreStatus': grpc.unary_unary_rpc_method_handler(
          servicer.RestoreStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syncagent__pb2.RestoreStatusResponse.SerializeToString,
      ),
      'SnapshotPurge': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotPurge,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotPurgeStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotPurgeStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syncagent__pb2.SnapshotPurgeStatusResponse.SerializeToString,
      ),
      'ReplicaRebuildStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ReplicaRebuildStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syncagent__pb2.ReplicaRebuildStatusResponse.SerializeToString,
      ),
      'SnapshotCloneStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotCloneStatus,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syncagent__pb2.SnapshotCloneStatusResponse.SerializeToString,
      ),
      'SnapshotHash': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHash,
          request_deserializer=syncagent__pb2.SnapshotHashRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotHashStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHashStatus,
          request_deserializer=syncagent__pb2.SnapshotHashStatusRequest.FromString,
          response_serializer=syncagent__pb2.SnapshotHashStatusResponse.SerializeToString,
      ),
      'SnapshotHashCancel': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHashCancel,
          request_deserializer=syncagent__pb2.SnapshotHashCancelRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SnapshotHashLockState': grpc.unary_unary_rpc_method_handler(
          servicer.SnapshotHashLockState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=syncagent__pb2.SnapshotHashLockStateResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ptypes.SyncAgentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))