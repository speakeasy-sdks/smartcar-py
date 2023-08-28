"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import securityread as shared_securityread
from typing import Optional



@dataclasses.dataclass
class GetVehiclesVehicleIDSecurityRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetVehiclesVehicleIDSecurityResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    security_read: Optional[shared_securityread.SecurityRead] = dataclasses.field(default=None)
    r"""Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available."""
    

