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
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetLocationRequest(
    vehicle_id="36ab27d0-fd9d-4455-823a-ce30af709ffc",
)
    
res = s.vehicles.get_location(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### compatibility

* `list_compatibility` - Compatibility

### evs

* `get_battery_capacity` - EV Battery Capacity
* `get_battery_level` - EV Battery Level
* `get_charging_status` - EV Charging Status

### vehicles

* `disconnect` - Revoke Access
* `get` - Vehicle Info
* `get_engine_oil` - Engine Oil Life
* `get_fuel_tank` - Fuel Tank (US Only)
* `get_location` - Location
* `get_odometer` - Odometer
* `get_permissions` - Application Permissions
* `get_tire_pressure` - Tire pressure
* `list_vehicles` - All Vehicles
* `lock_unlock` - Unlock Vehicle
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
