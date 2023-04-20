"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import permission as shared_permission
from typing import Optional


@dataclasses.dataclass
class GetPermissionsRequest:
    
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of vehicles to return"""  
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Index to start vehicle list at"""  
    vehicle_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetPermissionsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    permission: Optional[shared_permission.Permission] = dataclasses.field(default=None)
    r"""The applications permissions"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    