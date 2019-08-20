# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/compiler/tf2xla/host_compute_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/compiler/tf2xla/host_compute_metadata.proto',
  package='tensorflow.tf2xla',
  syntax='proto3',
  serialized_options=_b('\n\025org.tensorflow.tf2xlaB\014Tf2XlaProtosP\001\370\001\001'),
  serialized_pb=_b('\n6tensorflow/compiler/tf2xla/host_compute_metadata.proto\x12\x11tensorflow.tf2xla\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"a\n\x0eTensorMetadata\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\"X\n\x14HostTransferMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x08metadata\x18\x02 \x03(\x0b\x32!.tensorflow.tf2xla.TensorMetadata\"\x97\x01\n\x13HostComputeMetadata\x12?\n\x0e\x64\x65vice_to_host\x18\x01 \x03(\x0b\x32\'.tensorflow.tf2xla.HostTransferMetadata\x12?\n\x0ehost_to_device\x18\x02 \x03(\x0b\x32\'.tensorflow.tf2xla.HostTransferMetadataB*\n\x15org.tensorflow.tf2xlaB\x0cTf2XlaProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_TENSORMETADATA = _descriptor.Descriptor(
  name='TensorMetadata',
  full_name='tensorflow.tf2xla.TensorMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.tf2xla.TensorMetadata.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.tf2xla.TensorMetadata.shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=259,
)


_HOSTTRANSFERMETADATA = _descriptor.Descriptor(
  name='HostTransferMetadata',
  full_name='tensorflow.tf2xla.HostTransferMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.tf2xla.HostTransferMetadata.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow.tf2xla.HostTransferMetadata.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=349,
)


_HOSTCOMPUTEMETADATA = _descriptor.Descriptor(
  name='HostComputeMetadata',
  full_name='tensorflow.tf2xla.HostComputeMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_to_host', full_name='tensorflow.tf2xla.HostComputeMetadata.device_to_host', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_to_device', full_name='tensorflow.tf2xla.HostComputeMetadata.host_to_device', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=503,
)

_TENSORMETADATA.fields_by_name['type'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_TENSORMETADATA.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_HOSTTRANSFERMETADATA.fields_by_name['metadata'].message_type = _TENSORMETADATA
_HOSTCOMPUTEMETADATA.fields_by_name['device_to_host'].message_type = _HOSTTRANSFERMETADATA
_HOSTCOMPUTEMETADATA.fields_by_name['host_to_device'].message_type = _HOSTTRANSFERMETADATA
DESCRIPTOR.message_types_by_name['TensorMetadata'] = _TENSORMETADATA
DESCRIPTOR.message_types_by_name['HostTransferMetadata'] = _HOSTTRANSFERMETADATA
DESCRIPTOR.message_types_by_name['HostComputeMetadata'] = _HOSTCOMPUTEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorMetadata = _reflection.GeneratedProtocolMessageType('TensorMetadata', (_message.Message,), {
  'DESCRIPTOR' : _TENSORMETADATA,
  '__module__' : 'tensorflow.compiler.tf2xla.host_compute_metadata_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.TensorMetadata)
  })
_sym_db.RegisterMessage(TensorMetadata)

HostTransferMetadata = _reflection.GeneratedProtocolMessageType('HostTransferMetadata', (_message.Message,), {
  'DESCRIPTOR' : _HOSTTRANSFERMETADATA,
  '__module__' : 'tensorflow.compiler.tf2xla.host_compute_metadata_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.HostTransferMetadata)
  })
_sym_db.RegisterMessage(HostTransferMetadata)

HostComputeMetadata = _reflection.GeneratedProtocolMessageType('HostComputeMetadata', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCOMPUTEMETADATA,
  '__module__' : 'tensorflow.compiler.tf2xla.host_compute_metadata_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tf2xla.HostComputeMetadata)
  })
_sym_db.RegisterMessage(HostComputeMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)