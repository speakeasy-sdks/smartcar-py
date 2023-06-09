"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import compatibilityresponse as shared_compatibilityresponse
from typing import Optional


@dataclasses.dataclass
class ListCompatibilityRequest:
    
    country: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'country', 'style': 'form', 'explode': True }})  
    scope: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'scope', 'style': 'form', 'explode': True }})  
    vin: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'vin', 'style': 'form', 'explode': True }})  
    

@dataclasses.dataclass
class ListCompatibilityResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    compatibility_response: Optional[shared_compatibilityresponse.CompatibilityResponse] = dataclasses.field(default=None)
    r"""return Compatibility"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    