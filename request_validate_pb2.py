# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_validate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16request_validate.proto";\n\rEngineRequest\x12\x14\n\x0crequest_type\x18\x01 \x01(\t\x12\x14\n\x0crequest_data\x18\x02 \x01(\t"B\n\x0e\x45ngineResponse\x12\x17\n\x0fresponse_output\x18\x01 \x01(\t\x12\x17\n\x0fresponse_reason\x18\x02 \x03(\t2I\n\x0fValidateRequest\x12\x36\n\x11RequestValidation\x12\x0e.EngineRequest\x1a\x0f.EngineResponse"\x00\x62\x06proto3'
)


_ENGINEREQUEST = DESCRIPTOR.message_types_by_name["EngineRequest"]
_ENGINERESPONSE = DESCRIPTOR.message_types_by_name["EngineResponse"]
EngineRequest = _reflection.GeneratedProtocolMessageType(
    "EngineRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENGINEREQUEST,
        "__module__": "request_validate_pb2"
        # @@protoc_insertion_point(class_scope:EngineRequest)
    },
)
_sym_db.RegisterMessage(EngineRequest)

EngineResponse = _reflection.GeneratedProtocolMessageType(
    "EngineResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ENGINERESPONSE,
        "__module__": "request_validate_pb2"
        # @@protoc_insertion_point(class_scope:EngineResponse)
    },
)
_sym_db.RegisterMessage(EngineResponse)

_VALIDATEREQUEST = DESCRIPTOR.services_by_name["ValidateRequest"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _ENGINEREQUEST._serialized_start = 26
    _ENGINEREQUEST._serialized_end = 85
    _ENGINERESPONSE._serialized_start = 87
    _ENGINERESPONSE._serialized_end = 153
    _VALIDATEREQUEST._serialized_start = 155
    _VALIDATEREQUEST._serialized_end = 228
# @@protoc_insertion_point(module_scope)
