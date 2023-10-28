"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import chargelimit as shared_chargelimit
from typing import Optional


@dataclasses.dataclass
class GetChargingLimitRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetChargingLimitResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    charge_limit: Optional[shared_chargelimit.ChargeLimit] = dataclasses.field(default=None)
    r"""return EV Charge Limit"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

