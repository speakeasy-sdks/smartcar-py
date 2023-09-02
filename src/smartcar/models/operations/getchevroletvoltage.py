"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import chargevoltage as shared_chargevoltage
from typing import Optional



@dataclasses.dataclass
class GetChevroletVoltageRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetChevroletVoltageResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    charge_voltage: Optional[shared_chargevoltage.ChargeVoltage] = dataclasses.field(default=None)
    r"""returns the voltage of the charger measured by the vehicle."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
