"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import chargetime as shared_chargetime
from typing import Optional


@dataclasses.dataclass
class GetTeslaChargeTimeRequest:
    
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetTeslaChargeTimeResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    charge_time: Optional[shared_chargetime.ChargeTime] = dataclasses.field(default=None)
    r"""returns the date and time the vehicle expects to \\"complete\\" this charging session."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    