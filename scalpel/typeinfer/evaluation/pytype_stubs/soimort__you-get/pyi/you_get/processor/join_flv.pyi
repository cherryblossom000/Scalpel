# (generated with --quick)

import io
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

AMF_TYPE_AMF3_OBJECT: int
AMF_TYPE_ARRAY: int
AMF_TYPE_BOOLEAN: int
AMF_TYPE_CLASS_OBJECT: int
AMF_TYPE_DATE: int
AMF_TYPE_END_OF_OBJECT: int
AMF_TYPE_LONG_STRING: int
AMF_TYPE_MIXED_ARRAY: int
AMF_TYPE_MOVIECLIP: int
AMF_TYPE_NULL: int
AMF_TYPE_NUMBER: int
AMF_TYPE_OBJECT: int
AMF_TYPE_RECORDSET: int
AMF_TYPE_REFERENCE: int
AMF_TYPE_STRING: int
AMF_TYPE_UNDEFINED: int
AMF_TYPE_UNSUPPORTED: int
AMF_TYPE_XML: int
BytesIO: Type[io.BytesIO]
TAG_TYPE_METADATA: int
amf_readers: Dict[int, Callable[[Any], Any]]
amf_writers: Dict[int, Callable[[Any, Any], Any]]
amf_writers_tags: Dict[Type[Union[ECMAObject, bool, dict, float, list, str]], int]
struct: module

class ECMAObject:
    data: List[Tuple[Any, Any]]
    map: dict
    max_number: Any
    def __eq__(self, other) -> Any: ...
    def __init__(self, max_number) -> None: ...
    def __str__(self) -> str: ...
    def get(self, k) -> Any: ...
    def keys(self) -> dict_keys[nothing]: ...
    def put(self, k, v) -> None: ...
    def set(self, k, v) -> None: ...

def concat_flv(flvs, output = ...) -> Any: ...
def guess_output(inputs) -> Any: ...
def main() -> None: ...
def read_amf(stream) -> Any: ...
def read_amf_array(stream) -> list: ...
def read_amf_boolean(stream) -> bool: ...
def read_amf_mixed_array(stream) -> ECMAObject: ...
def read_amf_number(stream) -> Any: ...
def read_amf_object(stream) -> dict: ...
def read_amf_string(stream) -> Any: ...
def read_byte(stream) -> int: ...
def read_flv_header(stream) -> None: ...
def read_int(stream) -> Any: ...
def read_meta_data(stream) -> Tuple[Any, Any]: ...
def read_meta_tag(tag) -> Tuple[Any, Any]: ...
def read_tag(stream) -> Optional[Tuple[Any, Any, Any, Any, Any]]: ...
def read_uint(stream) -> Any: ...
def read_unsigned_medium_int(stream) -> Any: ...
def usage() -> None: ...
def write_amf(stream, v) -> None: ...
def write_amf_array(stream, o) -> None: ...
def write_amf_boolean(stream, v) -> None: ...
def write_amf_mixed_array(stream, o) -> None: ...
def write_amf_number(stream, v) -> None: ...
def write_amf_object(stream, o) -> None: ...
def write_amf_string(stream, s) -> None: ...
def write_byte(stream, b) -> None: ...
def write_flv_header(stream) -> None: ...
def write_meta_tag(stream, meta_type, meta_data) -> None: ...
def write_tag(stream, tag) -> None: ...
def write_uint(stream, n) -> None: ...