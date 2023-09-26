"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import vehicleinfo as shared_vehicleinfo
from typing import Optional



@dataclasses.dataclass
class GetVehicleRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetVehicleResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    vehicle_info: Optional[shared_vehicleinfo.VehicleInfo] = dataclasses.field(default=None)
    r"""A single vehicles"""
    

