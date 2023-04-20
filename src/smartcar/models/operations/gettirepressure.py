"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetTirePressureRequest:
    
    vehicle_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetTirePressureResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    