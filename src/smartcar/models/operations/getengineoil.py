"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import engineoil as shared_engineoil
from typing import Optional


@dataclasses.dataclass
class GetEngineOilRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetEngineOilResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    engine_oil: Optional[shared_engineoil.EngineOil] = dataclasses.field(default=None)
    r"""return engine oil reading"""
    

