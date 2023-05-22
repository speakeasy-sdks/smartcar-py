# cadillac

### Available Operations

* [get_charge_time](#get_charge_time) - Retrieve charging completion time for a Cadillac.
* [get_voltage](#get_voltage) - Retrieve charging voltmeter time for a Cadillac.

## get_charge_time

__Description__

When the vehicle is charging, this endpoint returns the date and time the vehicle expects to complete this charging session. When the vehicle is not charging, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.cadillac.get_charge_time('corrupti')

if res.charge_time is not None:
    # handle response
```

## get_voltage

__Description__

When the vehicle is plugged in, this endpoint returns the voltage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.cadillac.get_voltage('provident')

if res.charge_voltage is not None:
    # handle response
```
