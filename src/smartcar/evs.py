"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from smartcar import utils
from smartcar.models import errors, operations, shared
from typing import Optional

class Evs:
    r"""Operations about electric vehicles"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get_battery_capacity(self, vehicle_id: str) -> operations.GetBatteryCapacityResponse:
        r"""EV Battery Capacity
        __Description__

        Returns the total capacity of an electric vehicle's battery.

        __Permission__

        `read_battery`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  capacity|   number|  The total capacity of the vehicle's battery (in kilowatt-hours). 	|
        """
        request = operations.GetBatteryCapacityRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBatteryCapacityRequest, base_url, '/vehicles/{vehicle_id}/battery/capacity', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBatteryCapacityResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BatteryCapacity])
                res.battery_capacity = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_battery_level(self, vehicle_id: str) -> operations.GetBatteryLevelResponse:
        r"""EV Battery Level
        __Description__

        Retrieve EV battery level of a vehicle.

        __Permission__

        `read_battery`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  `percentRemaining`|   number|  An EV battery’s state of charge (in percent). 	|
        |   `range`|   number	|   The estimated remaining distance the vehicle can travel (in kilometers by default or in miles using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers).	|
        """
        request = operations.GetBatteryLevelRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBatteryLevelRequest, base_url, '/vehicles/{vehicle_id}/battery', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBatteryLevelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BatteryLevel])
                res.battery_level = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_charging_limit(self, vehicle_id: str) -> operations.GetChargingLimitResponse:
        r"""EV Charging Limit
        __Description__

        Returns the current charge limit of an electric vehicle.
        """
        request = operations.GetChargingLimitRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetChargingLimitRequest, base_url, '/vehicles/{vehicle_id}/charge/limit', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetChargingLimitResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ChargeLimit])
                res.charge_limit = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_charging_status(self, vehicle_id: str) -> operations.GetChargingStatusResponse:
        r"""EV Charging Status
        __Description__

        Returns the current charge status of an electric vehicle.

        __Permission__

        `read_charge`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  `isPluggedIn` 	|   boolean	|  Indicates whether a charging cable is currently plugged into the vehicle’s charge port. 	|
        |   `state`	|   string	|   Indicates whether the vehicle is currently charging. Options: `CHARGING` `FULLY_CHARGED` `NOT_CHARGING`	|
        """
        request = operations.GetChargingStatusRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetChargingStatusRequest, base_url, '/vehicles/{vehicle_id}/charge', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetChargingStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ChargeStatus])
                res.charge_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def set_charging_limit(self, vehicle_id: str, charge_limit: Optional[shared.ChargeLimit] = None) -> operations.SetChargingLimitResponse:
        r"""Set EV Charging Limit
        __Description__

        Returns the current charge limit of an electric vehicle.
        """
        request = operations.SetChargingLimitRequest(
            vehicle_id=vehicle_id,
            charge_limit=charge_limit,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.SetChargingLimitRequest, base_url, '/vehicles/{vehicle_id}/charge/limit', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "charge_limit", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SetChargingLimitResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def start_stop_charge(self, vehicle_id: str, charge_action: Optional[shared.ChargeAction] = None) -> operations.StartStopChargeResponse:
        r"""Start or stop charging an electric vehicle.
        __Description__

        Returns the current charge status of an electric vehicle.

        __Permission__

        `read_charge`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  `isPluggedIn` 	|   boolean	|  Indicates whether a charging cable is currently plugged into the vehicle’s charge port. 	|
        |   `state`	|   string	|   Indicates whether the vehicle is currently charging. Options: `CHARGING` `FULLY_CHARGED` `NOT_CHARGING`	|
        """
        request = operations.StartStopChargeRequest(
            vehicle_id=vehicle_id,
            charge_action=charge_action,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.StartStopChargeRequest, base_url, '/vehicles/{vehicle_id}/charge', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "charge_action", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.StartStopChargeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    