# Chevrolet
(*chevrolet*)

### Available Operations

* [get_charge_time](#get_charge_time) - Retrieve charging completion time for a Chevrolet.
* [get_voltage](#get_voltage) - Retrieve charging voltmeter time for a Chevrolet.

## get_charge_time

__Description__

When the vehicle is charging, this endpoint returns the date and time the vehicle expects to complete this charging session. When the vehicle is not charging, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.chevrolet.get_charge_time(vehicle_id='lightly')

if res.charge_time is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetChevroletChargeTimeResponse](../../models/operations/getchevroletchargetimeresponse.md)**


## get_voltage

__Description__

When the vehicle is plugged in, this endpoint returns the voltage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.chevrolet.get_voltage(vehicle_id='Global')

if res.charge_voltage is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetChevroletVoltageResponse](../../models/operations/getchevroletvoltageresponse.md)**

