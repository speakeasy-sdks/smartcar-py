"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deletedconnection as shared_deletedconnection
from typing import List, Optional

DELETE_MANAGEMENT_VEHICLE_CONNECTIONS_SERVERS = [
	"https://management.smartcar.com/v2.0",
    r"""Smartcar's Vehicle Management API"""
]


@dataclasses.dataclass
class DeleteManagementVehicleConnectionsSecurity:
    password: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic', 'field_name': 'password' }})
    username: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic', 'field_name': 'username' }})
    



@dataclasses.dataclass
class DeleteManagementVehicleConnectionsRequest:
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    r"""Delete all connections containing this user ID (UUID v4)."""
    vehicle_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'vehicle_id', 'style': 'form', 'explode': True }})
    r"""Delete all connections containing this vehicle ID (UUID v4)."""
    



@dataclasses.dataclass
class DeleteManagementVehicleConnectionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    deleted_connections_response: Optional[List[shared_deletedconnection.DeletedConnection]] = dataclasses.field(default=None)
    r"""returns all deleted connections"""
    

