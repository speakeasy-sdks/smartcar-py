<div align="center">
    <img src="https://user-images.githubusercontent.com/6267663/232771888-a65b182b-9ae7-42f3-9bbe-85658a61b9e3.svg" width="350px">
    <h1>Python SDK</h1>
   <p>Build and scale your mobility business</p>
   <a href="https://smartcar.com/docs/api/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/smartcar-py/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/smartcar-py/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/smartcar-py/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/smartcar-py?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/smartcar-py.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.vehicles.get_location('36ab27d0-fd9d-4455-823a-ce30af709ffc')

if res.location is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [cadillac](docs/cadillac/README.md)

* [get_charge_time](docs/cadillac/README.md#get_charge_time) - Retrieve charging completion time for a Cadillac.
* [get_voltage](docs/cadillac/README.md#get_voltage) - Retrieve charging voltmeter time for a Cadillac.

### [chevrolet](docs/chevrolet/README.md)

* [get_charge_time](docs/chevrolet/README.md#get_charge_time) - Retrieve charging completion time for a Chevrolet.
* [get_voltage](docs/chevrolet/README.md#get_voltage) - Retrieve charging voltmeter time for a Chevrolet.

### [compatibility](docs/compatibility/README.md)

* [list_compatibility](docs/compatibility/README.md#list_compatibility) - Compatibility

### [evs](docs/evs/README.md)

* [get_battery_capacity](docs/evs/README.md#get_battery_capacity) - EV Battery Capacity
* [get_battery_level](docs/evs/README.md#get_battery_level) - EV Battery Level
* [get_charging_limit](docs/evs/README.md#get_charging_limit) - EV Charging Limit
* [get_charging_status](docs/evs/README.md#get_charging_status) - EV Charging Status
* [set_charging_limit](docs/evs/README.md#set_charging_limit) - Set EV Charging Limit
* [start_stop_charge](docs/evs/README.md#start_stop_charge) - Start or stop charging an electric vehicle. Please contact us to request early access.

### [tesla](docs/tesla/README.md)

* [get_ammeter](docs/tesla/README.md#get_ammeter) - Retrieve charging ammeter time for a Tesla.
* [get_charge_time](docs/tesla/README.md#get_charge_time) - Retrieve charging completion time for a Tesla.
* [get_compass](docs/tesla/README.md#get_compass) - Retrieve compass heading for a Tesla.
* [get_exterior_temperature](docs/tesla/README.md#get_exterior_temperature) - Retrieve exterior temperature for a Tesla.
* [get_interior_temperature](docs/tesla/README.md#get_interior_temperature) - Retrieve interior temperature for a Tesla.
* [get_speedometer](docs/tesla/README.md#get_speedometer) - Retrieve speed for a Tesla.
* [get_voltage](docs/tesla/README.md#get_voltage) - Retrieve charging voltmeter time for a Tesla.
* [get_wattmeter](docs/tesla/README.md#get_wattmeter) - Retrieve charging wattmeter time for a Tesla.
* [set_ammeter](docs/tesla/README.md#set_ammeter) - Set charging ammeter time for a Tesla.

### [user](docs/user/README.md)

* [get_info](docs/user/README.md#get_info) - User Info

### [vehicles](docs/vehicles/README.md)

* [batch](docs/vehicles/README.md#batch) - Batch
* [disconnect](docs/vehicles/README.md#disconnect) - Revoke Access
* [get](docs/vehicles/README.md#get) - Vehicle Info
* [get_engine_oil](docs/vehicles/README.md#get_engine_oil) - Engine Oil Life
* [get_fuel_tank](docs/vehicles/README.md#get_fuel_tank) - Fuel Tank (US Only)
* [get_location](docs/vehicles/README.md#get_location) - Location
* [get_odometer](docs/vehicles/README.md#get_odometer) - Odometer
* [get_permissions](docs/vehicles/README.md#get_permissions) - Application Permissions
* [get_tire_pressure](docs/vehicles/README.md#get_tire_pressure) - Tire pressure
* [get_vin](docs/vehicles/README.md#get_vin) - Returns the vehicle’s manufacturer identifier.
* [list_vehicles](docs/vehicles/README.md#list_vehicles) - All Vehicles
* [lock_unlock](docs/vehicles/README.md#lock_unlock) - Lock/Unlock Vehicle

### [webhooks](docs/webhooks/README.md)

* [subscribe](docs/webhooks/README.md#subscribe) - Subscribe Webhook
* [unsubscribe](docs/webhooks/README.md#unsubscribe) - Unsubscribe Webhook
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
