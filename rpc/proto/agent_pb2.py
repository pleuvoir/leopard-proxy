# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61gent.proto\x12\x08services\x1a\x19google/protobuf/any.proto\"Q\n\tRpcResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0f\n\x07message\x18\x03 \x01(\t\"B\n\x10SubscribeRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\"$\n\x12UnSubscribeRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t2\x87\x01\n\x05\x41gent\x12<\n\tSubscribe\x12\x1a.services.SubscribeRequest\x1a\x13.services.RpcResult\x12@\n\x0bUnSubscribe\x12\x1c.services.UnSubscribeRequest\x1a\x13.services.RpcResultB\nZ\x08./;protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010./;proto'
  _RPCRESULT._serialized_start=52
  _RPCRESULT._serialized_end=133
  _SUBSCRIBEREQUEST._serialized_start=135
  _SUBSCRIBEREQUEST._serialized_end=201
  _UNSUBSCRIBEREQUEST._serialized_start=203
  _UNSUBSCRIBEREQUEST._serialized_end=239
  _AGENT._serialized_start=242
  _AGENT._serialized_end=377
# @@protoc_insertion_point(module_scope)
