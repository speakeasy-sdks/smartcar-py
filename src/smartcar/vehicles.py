"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from smartcar import utils
from smartcar.models import errors, operations, shared
from typing import Optional

class Vehicles:
    r"""Operations about vehicles"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def batch(self, vehicle_id: str, request_body: Optional[list[str]] = None) -> operations.BatchResponse:
        r"""Batch
        __Description__ Returns a list of responses from multiple Smartcar endpoints, all combined into a single request. Note: Batch requests is a paid feature. Please contact us to upgrade your plan and obtain access.
        """
        request = operations.BatchRequest(
            vehicle_id=vehicle_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.BatchRequest, base_url, '/vehicles/{vehicle_id}/batch', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.BatchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BatchResponse])
                res.batch_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def disconnect(self, vehicle_id: str) -> operations.DisconnectResponse:
        r"""Revoke Access
        __Description__

        Revoke access for the current requesting application. This is the correct way to disconnect a vehicle.

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|
        """
        request = operations.DisconnectRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DisconnectRequest, base_url, '/vehicles/{vehicle_id}/application', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DisconnectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DisconnectStatus])
                res.status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, vehicle_id: str) -> operations.GetVehicleResponse:
        r"""Vehicle Info
        __Permission__

        Returns a single vehicle object, containing identifying information.

        __Permission__

        `read_vehicle_info`

        __Response Body__

        |Name| Type|Description|
        |--|--|--|
        |`id`|string|A vehicle ID (UUID v4).|
        |`make`|string|The manufacturer of the vehicle.|
        |`model`|integer|The model of the vehicle.|
        |`year`|integer|The model year.|
        """
        request = operations.GetVehicleRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetVehicleRequest, base_url, '/vehicles/{vehicle_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetVehicleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VehicleInfo])
                res.vehicle_info = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_engine_oil(self, vehicle_id: str) -> operations.GetEngineOilResponse:
        r"""Engine Oil Life
        __Description__

        Returns the remaining life span of a vehicle’s engine oil.

        __Permission__

        `read_engine_oil`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  `lifeRemaining`|   number|  The engine oil’s remaining life span (as a percentage). Oil life is based on the current quality of the oil. (in percent).|
        """
        request = operations.GetEngineOilRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetEngineOilRequest, base_url, '/vehicles/{vehicle_id}/engine/oil', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetEngineOilResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EngineOil])
                res.engine_oil = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_fuel_tank(self, vehicle_id: str) -> operations.GetFuelTankResponse:
        r"""Fuel Tank (US Only)
        __Description__

        Returns the status of the fuel remaining in the vehicle’s gas tank. Note: The fuel tank API is only available for vehicles sold in the United States.

        __Permission__

        `read_fuel`

        __Response Body__

        |Name| Type|Desciprtion|
        |--|--|--|
        |`range`|number|The estimated remaining distance the car can travel (in kilometers by default or in miles using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        |`percentRemaining`|number|The remaining level of fuel in the tank (in percent).|
        |`amountRemaining`|number|The amount of fuel in the tank (in liters by default or in gallons (U.S.) using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        """
        request = operations.GetFuelTankRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetFuelTankRequest, base_url, '/vehicles/{vehicle_id}/fuel', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFuelTankResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FuelTank])
                res.fuel_tank = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_location(self, vehicle_id: str) -> operations.GetLocationResponse:
        r"""Location
        __Description__

        Retrieve latitude and longitude of a vehicle.

        __Permission__

        `read_location`

        __Response Body__

        |Name| Type|Desciprtion|
        |--|--|--|
        |`latitude`|number|The latitude (in degrees).|
        |`longitude`|number|The longitude (in degrees).|
        """
        request = operations.GetLocationRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetLocationRequest, base_url, '/vehicles/{vehicle_id}/location', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetLocationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Location])
                res.location = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_odometer(self, vehicle_id: str) -> operations.GetOdometerResponse:
        r"""Odometer
        __Description__

        Returns the vehicle’s last known odometer reading.

        __Permission__

        `read_odometer`

        __Response Body__

        |Name| Type|Desciprtion|
        |--|--|--|
        |`distance`|number|The current odometer of the vehicle (in kilometers by default or in miles using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        """
        request = operations.GetOdometerRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOdometerRequest, base_url, '/vehicles/{vehicle_id}/odometer', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOdometerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Odometer])
                res.odometer = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_permissions(self, vehicle_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> operations.GetPermissionsResponse:
        r"""Application Permissions
        __Description__

        Returns a list of the permissions that have been granted to your application in relation to this vehicle.

        __Query Parameters__

        |Parameter| Type|Required|Description|
        |--|--|--|--|
        |`limit`|integer|false|Number of permissions to return (default: 25).|
        |`offset`|integer|false|A vehicle ID (UUID v4).|Index to start permission list at|

        __Response Body__

        |Name| Type|Desciprtion|
        |--|--|--|
        |`permissions`|array|An array of permissions.|
        |`permissions.[]`|string|A permission.|
        |`paging`|object|Metadata about the current list of elements.|
        |`paging.count`|integer|The total number of elements for the entire query (not just the given page).|
        |`paging.offset`|integer|The current start index of the returned list of elements.|
        """
        request = operations.GetPermissionsRequest(
            vehicle_id=vehicle_id,
            limit=limit,
            offset=offset,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetPermissionsRequest, base_url, '/vehicles/{vehicle_id}/permissions', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetPermissionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPermissionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Permission])
                res.permission = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_tire_pressure(self, vehicle_id: str) -> operations.GetTirePressureResponse:
        r"""Tire pressure
        __Description__

        Returns the air pressure of each of the vehicle’s tires.
        __Permission__

        `read_tires`

        __Example Response__

        |Name| Type|Description|
        |--|--|--|
        |`frontLeft`|number|The current air pressure of the front left tire (in kilopascals by default or in pounds per square inch using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        |`frontRight`|number|The current air pressure of the front right tire (in kilopascals by default or in pounds per square inch using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        |`backLeft`|number|The current air pressure of the back left tire (in kilopascals by default or in pounds per square inch using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        |`backRight`|number|The current air pressure of the back right tire (in kilopascals by default or in pounds per square inch using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|
        """
        request = operations.GetTirePressureRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetTirePressureRequest, base_url, '/vehicles/{vehicle_id}/tires/pressure', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTirePressureResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TirePressure])
                res.tire_pressure = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_vin(self, vehicle_id: str) -> operations.GetVinResponse:
        r"""Returns the vehicle’s manufacturer identifier.
        __Description__

        Returns the vehicle’s manufacturer identifier.
        """
        request = operations.GetVinRequest(
            vehicle_id=vehicle_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetVinRequest, base_url, '/vehicles/{vehicle_id}/vin', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetVinResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VinInfo])
                res.vin_info = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list_vehicles(self, limit: Optional[int] = None, offset: Optional[int] = None) -> operations.ListVehiclesResponse:
        r"""All Vehicles
        __Description__

        Returns a paged list of all vehicles connected to the application for the current authorized user.

        __Query Parameters__

        |Parameter| Type|Required|Description|
        |--|--|--|--|
        |`limit`|integer|false|Number of vehicles to return (default: 10).|
        |`offset`|integer|false|A vehicle ID (UUID v4).|Index to start vehicle list at|

        __Response Body__

        |Name| Type|Desciprtion|
        |--|--|--|
        |`vehicles`|array|An array of vehicle IDs.|
        |`vehicles.[]`|string|A vehicle ID (UUID v4).|
        |`paging`|object|Metadata about the current list of elements.|
        |`paging.count`|integer|The total number of elements for the entire query (not just the given page).|
        |`paging.offset`|integer|The current start index of the returned list of elements.|
        """
        request = operations.ListVehiclesRequest(
            limit=limit,
            offset=offset,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/vehicles'
        headers = {}
        query_params = utils.get_query_params(operations.ListVehiclesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListVehiclesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VehiclesResponse])
                res.vehicles_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def lock_unlock(self, vehicle_id: str, security_action: Optional[shared.SecurityAction] = None) -> operations.LockUnlockResponse:
        r"""Lock/Unlock Vehicle
        __Description__

        Unlock the vehicle

        __Permission__

        `control_security`

        __Response body__

        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|
        """
        request = operations.LockUnlockRequest(
            vehicle_id=vehicle_id,
            security_action=security_action,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.LockUnlockRequest, base_url, '/vehicles/{vehicle_id}/security', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "security_action", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.LockUnlockResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    