"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class DisconnectRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    


class DisconnectStatus(str, Enum):
    r"""Revoke application access"""
    SUCCESS = 'success'



@dataclasses.dataclass
class DisconnectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[DisconnectStatus] = dataclasses.field(default=None)
    r"""Revoke application access"""
    

