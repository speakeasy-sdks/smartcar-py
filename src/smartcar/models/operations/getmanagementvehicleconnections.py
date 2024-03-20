"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connectionsresponse as shared_connectionsresponse
from typing import Optional

GET_MANAGEMENT_VEHICLE_CONNECTIONS_SERVERS = [
	"https://management.smartcar.com/v2.0",
    r"""Smartcar's Vehicle Management API"""
]


@dataclasses.dataclass
class GetManagementVehicleConnectionsRequest:
    cursor: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Used for accessing pages other than the first page. Each page returned has a cursor value that can be passed here to fetch the “next” page."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Number of connections to return (default: 10, maximum: 100)."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    r"""Filter for connections created by the provider user ID."""
    vehicle_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'vehicle_id', 'style': 'form', 'explode': True }})
    r"""Filter for connections to the provided vehicle ID."""
    



@dataclasses.dataclass
class GetManagementVehicleConnectionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connections_response: Optional[shared_connectionsresponse.ConnectionsResponse] = dataclasses.field(default=None)
    r"""returns vehicle connections"""
    

