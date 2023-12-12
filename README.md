<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/232771888-a65b182b-9ae7-42f3-9bbe-85658a61b9e3.svg" width="350px">
    <h1>Python SDK</h1>
   <p>Build and scale your mobility business</p>
   <a href="https://smartcar.com/docs/api/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/smartcar-py/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/smartcar-py/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/smartcar-py/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/smartcar-py?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/smartcar-py.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import smartcar
from smartcar.models import operations, shared

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [compatibility](docs/sdks/compatibility/README.md)

* [list_compatibility](docs/sdks/compatibility/README.md#list_compatibility) - Compatibility

### [vehicle_management](docs/sdks/vehiclemanagement/README.md)

* [delete_management_vehicle_connections](docs/sdks/vehiclemanagement/README.md#delete_management_vehicle_connections) - Delete vehicle connections by user_id or vehicle_id
* [get_management_vehicle_connections](docs/sdks/vehiclemanagement/README.md#get_management_vehicle_connections) - Retrieve vehicle connections

### [user](docs/sdks/user/README.md)

* [get_info](docs/sdks/user/README.md#get_info) - User Info

### [vehicles](docs/sdks/vehicles/README.md)

* [batch](docs/sdks/vehicles/README.md#batch) - Batch
* [disconnect](docs/sdks/vehicles/README.md#disconnect) - Revoke Access
* [get](docs/sdks/vehicles/README.md#get) - Vehicle Info
* [get_engine_oil](docs/sdks/vehicles/README.md#get_engine_oil) - Engine Oil Life
* [get_fuel_tank](docs/sdks/vehicles/README.md#get_fuel_tank) - Fuel Tank (US Only)
* [get_location](docs/sdks/vehicles/README.md#get_location) - Location
* [get_odometer](docs/sdks/vehicles/README.md#get_odometer) - Odometer
* [get_permissions](docs/sdks/vehicles/README.md#get_permissions) - Application Permissions
* [get_tire_pressure](docs/sdks/vehicles/README.md#get_tire_pressure) - Tire Pressure
* [get_vin](docs/sdks/vehicles/README.md#get_vin) - Returns the vehicle’s manufacturer identifier.
* [get_vehicles_vehicle_id_security](docs/sdks/vehicles/README.md#get_vehicles_vehicle_id_security) - Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available. The open status array(s) will be empty if a vehicle has partial support. The request will error if lock status can not be retrieved from the vehicle or the brand is not supported.
* [list_vehicles](docs/sdks/vehicles/README.md#list_vehicles) - All Vehicles
* [lock_unlock](docs/sdks/vehicles/README.md#lock_unlock) - Lock/Unlock Vehicle

### [tesla](docs/sdks/tesla/README.md)

* [get_ammeter](docs/sdks/tesla/README.md#get_ammeter) - Retrieve charging ammeter time for a Tesla.
* [get_charge_time](docs/sdks/tesla/README.md#get_charge_time) - Retrieve charging completion time for a Tesla.
* [get_compass](docs/sdks/tesla/README.md#get_compass) - Retrieve compass heading for a Tesla.
* [get_exterior_temperature](docs/sdks/tesla/README.md#get_exterior_temperature) - Retrieve exterior temperature for a Tesla.
* [get_interior_temperature](docs/sdks/tesla/README.md#get_interior_temperature) - Retrieve interior temperature for a Tesla.
* [get_speedometer](docs/sdks/tesla/README.md#get_speedometer) - Retrieve speed for a Tesla.
* [get_voltage](docs/sdks/tesla/README.md#get_voltage) - Retrieve charging voltmeter time for a Tesla.
* [get_wattmeter](docs/sdks/tesla/README.md#get_wattmeter) - Retrieve charging wattmeter time for a Tesla.
* [set_ammeter](docs/sdks/tesla/README.md#set_ammeter) - Set charging ammeter time for a Tesla.

### [evs](docs/sdks/evs/README.md)

* [get_battery_capacity](docs/sdks/evs/README.md#get_battery_capacity) - EV Battery Capacity
* [get_battery_level](docs/sdks/evs/README.md#get_battery_level) - EV Battery Level
* [get_charging_limit](docs/sdks/evs/README.md#get_charging_limit) - EV Charging Limit
* [get_charging_status](docs/sdks/evs/README.md#get_charging_status) - EV Charging Status
* [set_charging_limit](docs/sdks/evs/README.md#set_charging_limit) - Set EV Charging Limit
* [start_stop_charge](docs/sdks/evs/README.md#start_stop_charge) - Start or stop charging an electric vehicle.

### [cadillac](docs/sdks/cadillac/README.md)

* [get_charge_time](docs/sdks/cadillac/README.md#get_charge_time) - Retrieve charging completion time for a Cadillac.
* [get_voltage](docs/sdks/cadillac/README.md#get_voltage) - Retrieve charging voltmeter time for a Cadillac.

### [chevrolet](docs/sdks/chevrolet/README.md)

* [get_charge_time](docs/sdks/chevrolet/README.md#get_charge_time) - Retrieve charging completion time for a Chevrolet.
* [get_voltage](docs/sdks/chevrolet/README.md#get_voltage) - Retrieve charging voltmeter time for a Chevrolet.

### [webhooks](docs/sdks/webhooks/README.md)

* [subscribe](docs/sdks/webhooks/README.md#subscribe) - Subscribe Webhook
* [unsubscribe](docs/sdks/webhooks/README.md#unsubscribe) - Unsubscribe Webhook
<!-- End Available Resources and Operations [operations] -->





<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = None
try:
    res = s.compatibility.list_compatibility(country='{country}', scope='{scope}', vin='{vin}')
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.compatibility_response is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.smartcar.com/v2.0` | None |

#### Example

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    server_idx=0,
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.compatibility.list_compatibility(country='{country}', scope='{scope}', vin='{vin}')

if res.compatibility_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    server_url="https://api.smartcar.com/v2.0",
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.compatibility.list_compatibility(country='{country}', scope='{scope}', vin='{vin}')

if res.compatibility_response is not None:
    # handle response
    pass
```

### Override Server URL Per-Operation

The server URL can also be overridden on a per-operation basis, provided a server list was specified for the operation. For example:
```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar()


res = s.vehicle_management.delete_management_vehicle_connections(operations.DeleteManagementVehicleConnectionsSecurity(
    password="<YOUR_PASSWORD_HERE>",
    username="<YOUR_USERNAME_HERE>",
), server_url="https://management.smartcar.com/v2.0", user_id='string', vehicle_id='string')

if res.deleted_connections_response is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import smartcar
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = smartcar.Smartcar(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `basic_auth`  | http          | HTTP Basic    |
| `bearer_auth` | http          | HTTP Bearer   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.compatibility.list_compatibility(country='{country}', scope='{scope}', vin='{vin}')

if res.compatibility_response is not None:
    # handle response
    pass
```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar()


res = s.vehicle_management.delete_management_vehicle_connections(operations.DeleteManagementVehicleConnectionsSecurity(
    password="<YOUR_PASSWORD_HERE>",
    username="<YOUR_USERNAME_HERE>",
), user_id='string', vehicle_id='string')

if res.deleted_connections_response is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
