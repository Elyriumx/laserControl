from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLaserStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetLaserStatusResponse(_message.Message):
    __slots__ = ["status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        OFF: _ClassVar[GetLaserStatusResponse.Status]
        ON: _ClassVar[GetLaserStatusResponse.Status]
    OFF: GetLaserStatusResponse.Status
    ON: GetLaserStatusResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: GetLaserStatusResponse.Status
    def __init__(self, status: _Optional[_Union[GetLaserStatusResponse.Status, str]] = ...) -> None: ...

class SetBiasVoltageRequest(_message.Message):
    __slots__ = ["voltage"]
    VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    voltage: float
    def __init__(self, voltage: _Optional[float] = ...) -> None: ...

class SetBiasVoltageResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class EnableLaserRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EnableLaserResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class DisableLaserRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DisableLaserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
