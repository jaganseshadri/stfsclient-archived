# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/xla/rpc/xla_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.compiler.xla import xla_pb2 as tensorflow_dot_compiler_dot_xla_dot_xla__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/compiler/xla/rpc/xla_service.proto',
  package='xla',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-tensorflow/compiler/xla/rpc/xla_service.proto\x12\x03xla\x1a!tensorflow/compiler/xla/xla.proto2\xea\n\n\nXlaService\x12?\n\nUnregister\x12\x16.xla.UnregisterRequest\x1a\x17.xla.UnregisterResponse\"\x00\x12Q\n\x10\x44\x65\x63onstructTuple\x12\x1c.xla.DeconstructTupleRequest\x1a\x1d.xla.DeconstructTupleResponse\"\x00\x12\x33\n\x06Unpack\x12\x12.xla.UnpackRequest\x1a\x13.xla.UnpackResponse\"\x00\x12\x39\n\x08GetShape\x12\x14.xla.GetShapeRequest\x1a\x15.xla.GetShapeResponse\"\x00\x12^\n\x18GetComputationGraphStats\x12!.xla.ComputationGraphStatsRequest\x1a\x1d.xla.ComputationStatsResponse\"\x00\x12\x39\n\x08LoadData\x12\x14.xla.LoadDataRequest\x1a\x15.xla.LoadDataResponse\"\x00\x12Q\n\x10TransferToClient\x12\x1c.xla.TransferToClientRequest\x1a\x1d.xla.TransferToClientResponse\"\x00\x12Q\n\x10TransferToServer\x12\x1c.xla.TransferToServerRequest\x1a\x1d.xla.TransferToServerResponse\"\x00\x12Q\n\x10TransferToInfeed\x12\x1c.xla.TransferToInfeedRequest\x1a\x1d.xla.TransferToInfeedResponse\"\x00\x12Z\n\x13TransferFromOutfeed\x12\x1f.xla.TransferFromOutfeedRequest\x1a .xla.TransferFromOutfeedResponse\"\x00\x12\x42\n\x0bResetDevice\x12\x17.xla.ResetDeviceRequest\x1a\x18.xla.ResetDeviceResponse\"\x00\x12X\n\x14\x43omputeConstantGraph\x12 .xla.ComputeConstantGraphRequest\x1a\x1c.xla.ComputeConstantResponse\"\x00\x12Q\n\x10GetDeviceHandles\x12\x1c.xla.GetDeviceHandlesRequest\x1a\x1d.xla.GetDeviceHandlesResponse\"\x00\x12Z\n\x13\x43reateChannelHandle\x12\x1f.xla.CreateChannelHandleRequest\x1a .xla.CreateChannelHandleResponse\"\x00\x12\x36\n\x07\x43ompile\x12\x13.xla.CompileRequest\x1a\x14.xla.CompileResponse\"\x00\x12\x36\n\x07\x45xecute\x12\x13.xla.ExecuteRequest\x1a\x14.xla.ExecuteResponse\"\x00\x12X\n\x14\x45xecuteGraphParallel\x12 .xla.ExecuteGraphParallelRequest\x1a\x1c.xla.ExecuteParallelResponse\"\x00\x12Q\n\x10WaitForExecution\x12\x1c.xla.WaitForExecutionRequest\x1a\x1d.xla.WaitForExecutionResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_compiler_dot_xla_dot_xla__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_XLASERVICE = _descriptor.ServiceDescriptor(
  name='XlaService',
  full_name='xla.XlaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=90,
  serialized_end=1476,
  methods=[
  _descriptor.MethodDescriptor(
    name='Unregister',
    full_name='xla.XlaService.Unregister',
    index=0,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._UNREGISTERREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._UNREGISTERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeconstructTuple',
    full_name='xla.XlaService.DeconstructTuple',
    index=1,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._DECONSTRUCTTUPLEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._DECONSTRUCTTUPLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Unpack',
    full_name='xla.XlaService.Unpack',
    index=2,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._UNPACKREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._UNPACKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShape',
    full_name='xla.XlaService.GetShape',
    index=3,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._GETSHAPEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._GETSHAPERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetComputationGraphStats',
    full_name='xla.XlaService.GetComputationGraphStats',
    index=4,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPUTATIONGRAPHSTATSREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPUTATIONSTATSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LoadData',
    full_name='xla.XlaService.LoadData',
    index=5,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._LOADDATAREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._LOADDATARESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferToClient',
    full_name='xla.XlaService.TransferToClient',
    index=6,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOCLIENTREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOCLIENTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferToServer',
    full_name='xla.XlaService.TransferToServer',
    index=7,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOSERVERREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOSERVERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferToInfeed',
    full_name='xla.XlaService.TransferToInfeed',
    index=8,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOINFEEDREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERTOINFEEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferFromOutfeed',
    full_name='xla.XlaService.TransferFromOutfeed',
    index=9,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERFROMOUTFEEDREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._TRANSFERFROMOUTFEEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetDevice',
    full_name='xla.XlaService.ResetDevice',
    index=10,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._RESETDEVICEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._RESETDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ComputeConstantGraph',
    full_name='xla.XlaService.ComputeConstantGraph',
    index=11,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPUTECONSTANTGRAPHREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPUTECONSTANTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDeviceHandles',
    full_name='xla.XlaService.GetDeviceHandles',
    index=12,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._GETDEVICEHANDLESREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._GETDEVICEHANDLESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateChannelHandle',
    full_name='xla.XlaService.CreateChannelHandle',
    index=13,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._CREATECHANNELHANDLEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._CREATECHANNELHANDLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Compile',
    full_name='xla.XlaService.Compile',
    index=14,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPILEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._COMPILERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='xla.XlaService.Execute',
    index=15,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._EXECUTEREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._EXECUTERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ExecuteGraphParallel',
    full_name='xla.XlaService.ExecuteGraphParallel',
    index=16,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._EXECUTEGRAPHPARALLELREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._EXECUTEPARALLELRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WaitForExecution',
    full_name='xla.XlaService.WaitForExecution',
    index=17,
    containing_service=None,
    input_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._WAITFOREXECUTIONREQUEST,
    output_type=tensorflow_dot_compiler_dot_xla_dot_xla__pb2._WAITFOREXECUTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_XLASERVICE)

DESCRIPTOR.services_by_name['XlaService'] = _XLASERVICE

# @@protoc_insertion_point(module_scope)
