# Vehicles
(*vehicles*)

## Overview

Operations about vehicles

### Available Operations

* [batch](#batch) - Batch
* [disconnect](#disconnect) - Revoke Access
* [get](#get) - Vehicle Info
* [get_engine_oil](#get_engine_oil) - Engine Oil Life
* [get_fuel_tank](#get_fuel_tank) - Fuel Tank (US Only)
* [get_location](#get_location) - Location
* [get_odometer](#get_odometer) - Odometer
* [get_permissions](#get_permissions) - Application Permissions
* [get_tire_pressure](#get_tire_pressure) - Tire Pressure
* [get_vin](#get_vin) - Returns the vehicle’s manufacturer identifier.
* [get_vehicles_vehicle_id_security](#get_vehicles_vehicle_id_security) - Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available. The open status array(s) will be empty if a vehicle has partial support. The request will error if lock status can not be retrieved from the vehicle or the brand is not supported.
* [list_vehicles](#list_vehicles) - All Vehicles
* [lock_unlock](#lock_unlock) - Lock/Unlock Vehicle

## batch

__Description__ Returns a list of responses from multiple Smartcar endpoints, all combined into a single request. Note: Batch requests is a paid feature. Please contact us to upgrade your plan and obtain access.

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.batch(vehicle_id='<value>', request_body=[
    '/odometer',
])

if res.batch_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |
| `request_body`     | List[*str*]        | :heavy_minus_sign: | N/A                |


### Response

**[operations.BatchResponse](../../models/operations/batchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## disconnect

__Description__

Revoke access for the current requesting application. This is the correct way to disconnect a vehicle.

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.disconnect(vehicle_id='<value>')

if res.status is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DisconnectResponse](../../models/operations/disconnectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

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

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get(vehicle_id='<value>')

if res.vehicle_info is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetVehicleResponse](../../models/operations/getvehicleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_engine_oil

__Description__

Returns the remaining life span of a vehicle’s engine oil.

__Permission__

`read_engine_oil`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  `lifeRemaining`|   number|  The engine oil’s remaining life span (as a percentage). Oil life is based on the current quality of the oil. (in percent).|

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_engine_oil(vehicle_id='<value>')

if res.engine_oil is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetEngineOilResponse](../../models/operations/getengineoilresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_fuel_tank

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

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_fuel_tank(vehicle_id='<value>')

if res.fuel_tank is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetFuelTankResponse](../../models/operations/getfueltankresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_location

__Description__

Retrieve latitude and longitude of a vehicle.

__Permission__

`read_location`

__Response Body__

|Name| Type|Desciprtion|
|--|--|--|
|`latitude`|number|The latitude (in degrees).|
|`longitude`|number|The longitude (in degrees).|

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_location(vehicle_id='36ab27d0-fd9d-4455-823a-ce30af709ffc')

if res.location is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `vehicle_id`                         | *str*                                | :heavy_check_mark:                   | N/A                                  | 36ab27d0-fd9d-4455-823a-ce30af709ffc |


### Response

**[operations.GetLocationResponse](../../models/operations/getlocationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_odometer

__Description__

Returns the vehicle’s last known odometer reading.

__Permission__

`read_odometer`

__Response Body__

|Name| Type|Desciprtion|
|--|--|--|
|`distance`|number|The current odometer of the vehicle (in kilometers by default or in miles using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers)).|

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_odometer(vehicle_id='<value>')

if res.odometer is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetOdometerResponse](../../models/operations/getodometerresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_permissions

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

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_permissions(vehicle_id='<value>', limit=362662, offset=729387)

if res.permission is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `vehicle_id`                   | *str*                          | :heavy_check_mark:             | N/A                            |
| `limit`                        | *Optional[int]*                | :heavy_minus_sign:             | Number of vehicles to return   |
| `offset`                       | *Optional[int]*                | :heavy_minus_sign:             | Index to start vehicle list at |


### Response

**[operations.GetPermissionsResponse](../../models/operations/getpermissionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_tire_pressure

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

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_tire_pressure(vehicle_id='<value>')

if res.tire_pressure is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTirePressureResponse](../../models/operations/gettirepressureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_vin

__Description__

Returns the vehicle’s manufacturer identifier.

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_vin(vehicle_id='<value>')

if res.vin_info is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetVinResponse](../../models/operations/getvinresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_vehicles_vehicle_id_security

Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available. The open status array(s) will be empty if a vehicle has partial support. The request will error if lock status can not be retrieved from the vehicle or the brand is not supported.

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_vehicles_vehicle_id_security(vehicle_id='<value>')

if res.security_read is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetVehiclesVehicleIDSecurityResponse](../../models/operations/getvehiclesvehicleidsecurityresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_vehicles

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

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.list_vehicles(limit=568500, offset=311354)

if res.vehicles_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `limit`                        | *Optional[int]*                | :heavy_minus_sign:             | Number of vehicles to return   |
| `offset`                       | *Optional[int]*                | :heavy_minus_sign:             | Index to start vehicle list at |


### Response

**[operations.ListVehiclesResponse](../../models/operations/listvehiclesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## lock_unlock

__Description__

Unlock the vehicle

__Permission__

`control_security`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.lock_unlock(vehicle_id='<value>', security_action=shared.SecurityAction(
    action=shared.SecurityActionAction.UNLOCK,
))

if res.success_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `vehicle_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `security_action`                                                        | [Optional[shared.SecurityAction]](../../models/shared/securityaction.md) | :heavy_minus_sign:                                                       | N/A                                                                      |


### Response

**[operations.LockUnlockResponse](../../models/operations/lockunlockresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
