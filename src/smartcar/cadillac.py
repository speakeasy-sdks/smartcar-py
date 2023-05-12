"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from smartcar.models import operations, shared
from typing import Optional

class Cadillac:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def get_charge_time(self, vehicle_id: str) -> operations.GetCadillacChargeTimeResponse:
        r"""Retrieve charging completion time for a Cadillac.
        __Description__
        
        When the vehicle is charging, this endpoint returns the date and time the vehicle expects to complete this charging session. When the vehicle is not charging, this endpoint results in a vehicle state error.
        """
        request = operations.GetCadillacChargeTimeRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCadillacChargeTimeRequest, base_url, '/vehicles/{vehicle_id}/cadillac/charge/completion', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCadillacChargeTimeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ChargeTime])
                res.charge_time = out

        return res

    
    def get_voltage(self, vehicle_id: str) -> operations.GetCadillacVoltageResponse:
        r"""Retrieve charging voltmeter time for a Cadillac.
        __Description__
        
        When the vehicle is plugged in, this endpoint returns the voltage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.
        """
        request = operations.GetCadillacVoltageRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetCadillacVoltageRequest, base_url, '/vehicles/{vehicle_id}/cadillac/charge/voltmeter', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCadillacVoltageResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ChargeVoltage])
                res.charge_voltage = out

        return res

    