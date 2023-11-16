"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import chargetime as shared_chargetime
from typing import Optional


@dataclasses.dataclass
class GetChevroletChargeTimeRequest:
    vehicle_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vehicle_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetChevroletChargeTimeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    charge_time: Optional[shared_chargetime.ChargeTime] = dataclasses.field(default=None)
    r"""returns the date and time the vehicle expects to \\"complete\\" this charging session."""
    

