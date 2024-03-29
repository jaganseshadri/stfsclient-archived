# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from tensorflow.core.protobuf import worker_pb2 as tensorflow_dot_core_dot_protobuf_dot_worker__pb2


class WorkerServiceStub(object):
  """//////////////////////////////////////////////////////////////////////////////

  WorkerService defines a TensorFlow service that executes dataflow
  graphs on a set of local devices, on behalf of a MasterService.

  A worker service keeps track of multiple "registered graphs". Each
  registered graph is a subgraph of a client's graph, corresponding to
  only the nodes that should execute on this worker (and any
  additional nodes necessary for inter-process communication using
  the `RecvTensor` method).

  //////////////////////////////////////////////////////////////////////////////

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStatus = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/GetStatus',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStatusRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStatusResponse.FromString,
        )
    self.CreateWorkerSession = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/CreateWorkerSession',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CreateWorkerSessionRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CreateWorkerSessionResponse.FromString,
        )
    self.DeleteWorkerSession = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/DeleteWorkerSession',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeleteWorkerSessionRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeleteWorkerSessionResponse.FromString,
        )
    self.RegisterGraph = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/RegisterGraph',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RegisterGraphRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RegisterGraphResponse.FromString,
        )
    self.DeregisterGraph = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/DeregisterGraph',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeregisterGraphRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeregisterGraphResponse.FromString,
        )
    self.RunGraph = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/RunGraph',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RunGraphRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RunGraphResponse.FromString,
        )
    self.CleanupGraph = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/CleanupGraph',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupGraphRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupGraphResponse.FromString,
        )
    self.CleanupAll = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/CleanupAll',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupAllRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupAllResponse.FromString,
        )
    self.RecvTensor = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/RecvTensor',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvTensorRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvTensorResponse.FromString,
        )
    self.Logging = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/Logging',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.LoggingRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.LoggingResponse.FromString,
        )
    self.Tracing = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/Tracing',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.TracingRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.TracingResponse.FromString,
        )
    self.RecvBuf = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/RecvBuf',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvBufRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvBufResponse.FromString,
        )
    self.GetStepSequence = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/GetStepSequence',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStepSequenceRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStepSequenceResponse.FromString,
        )
    self.CompleteGroup = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/CompleteGroup',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteGroupRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteGroupResponse.FromString,
        )
    self.CompleteInstance = channel.unary_unary(
        '/tensorflow.grpc.WorkerService/CompleteInstance',
        request_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteInstanceRequest.SerializeToString,
        response_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteInstanceResponse.FromString,
        )


class WorkerServiceServicer(object):
  """//////////////////////////////////////////////////////////////////////////////

  WorkerService defines a TensorFlow service that executes dataflow
  graphs on a set of local devices, on behalf of a MasterService.

  A worker service keeps track of multiple "registered graphs". Each
  registered graph is a subgraph of a client's graph, corresponding to
  only the nodes that should execute on this worker (and any
  additional nodes necessary for inter-process communication using
  the `RecvTensor` method).

  //////////////////////////////////////////////////////////////////////////////

  """

  def GetStatus(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateWorkerSession(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteWorkerSession(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterGraph(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeregisterGraph(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunGraph(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CleanupGraph(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CleanupAll(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecvTensor(self, request, context):
    """See worker.proto for details.
    RecvTensor Method
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Logging(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Tracing(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecvBuf(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStepSequence(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompleteGroup(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CompleteInstance(self, request, context):
    """See worker.proto for details.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStatusRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStatusResponse.SerializeToString,
      ),
      'CreateWorkerSession': grpc.unary_unary_rpc_method_handler(
          servicer.CreateWorkerSession,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CreateWorkerSessionRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CreateWorkerSessionResponse.SerializeToString,
      ),
      'DeleteWorkerSession': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteWorkerSession,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeleteWorkerSessionRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeleteWorkerSessionResponse.SerializeToString,
      ),
      'RegisterGraph': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterGraph,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RegisterGraphRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RegisterGraphResponse.SerializeToString,
      ),
      'DeregisterGraph': grpc.unary_unary_rpc_method_handler(
          servicer.DeregisterGraph,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeregisterGraphRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.DeregisterGraphResponse.SerializeToString,
      ),
      'RunGraph': grpc.unary_unary_rpc_method_handler(
          servicer.RunGraph,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RunGraphRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RunGraphResponse.SerializeToString,
      ),
      'CleanupGraph': grpc.unary_unary_rpc_method_handler(
          servicer.CleanupGraph,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupGraphRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupGraphResponse.SerializeToString,
      ),
      'CleanupAll': grpc.unary_unary_rpc_method_handler(
          servicer.CleanupAll,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupAllRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CleanupAllResponse.SerializeToString,
      ),
      'RecvTensor': grpc.unary_unary_rpc_method_handler(
          servicer.RecvTensor,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvTensorRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvTensorResponse.SerializeToString,
      ),
      'Logging': grpc.unary_unary_rpc_method_handler(
          servicer.Logging,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.LoggingRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.LoggingResponse.SerializeToString,
      ),
      'Tracing': grpc.unary_unary_rpc_method_handler(
          servicer.Tracing,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.TracingRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.TracingResponse.SerializeToString,
      ),
      'RecvBuf': grpc.unary_unary_rpc_method_handler(
          servicer.RecvBuf,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvBufRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.RecvBufResponse.SerializeToString,
      ),
      'GetStepSequence': grpc.unary_unary_rpc_method_handler(
          servicer.GetStepSequence,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStepSequenceRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.GetStepSequenceResponse.SerializeToString,
      ),
      'CompleteGroup': grpc.unary_unary_rpc_method_handler(
          servicer.CompleteGroup,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteGroupRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteGroupResponse.SerializeToString,
      ),
      'CompleteInstance': grpc.unary_unary_rpc_method_handler(
          servicer.CompleteInstance,
          request_deserializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteInstanceRequest.FromString,
          response_serializer=tensorflow_dot_core_dot_protobuf_dot_worker__pb2.CompleteInstanceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.grpc.WorkerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
