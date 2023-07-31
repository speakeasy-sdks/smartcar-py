"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import batterylevel as shared_batterylevel
from typing import Optional



@dataclasses.dataclass
class GetBatteryLevelRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetBatteryLevelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    battery_level: Optional[shared_batterylevel.BatteryLevel] = dataclasses.field(default=None)
    r"""return EV Battery Level reading"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

