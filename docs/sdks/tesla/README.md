# tesla

### Available Operations

* [get_ammeter](#get_ammeter) - Retrieve charging ammeter time for a Tesla.
* [get_charge_time](#get_charge_time) - Retrieve charging completion time for a Tesla.
* [get_compass](#get_compass) - Retrieve compass heading for a Tesla.
* [get_exterior_temperature](#get_exterior_temperature) - Retrieve exterior temperature for a Tesla.
* [get_interior_temperature](#get_interior_temperature) - Retrieve interior temperature for a Tesla.
* [get_speedometer](#get_speedometer) - Retrieve speed for a Tesla.
* [get_voltage](#get_voltage) - Retrieve charging voltmeter time for a Tesla.
* [get_wattmeter](#get_wattmeter) - Retrieve charging wattmeter time for a Tesla.
* [set_ammeter](#set_ammeter) - Set charging ammeter time for a Tesla.

## get_ammeter

__Description__

When the vehicle is plugged in, this endpoint returns the amperage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_ammeter('deserunt')

if res.charge_ammeter is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaAmmeterResponse](../../models/operations/getteslaammeterresponse.md)**


## get_charge_time

__Description__

When the vehicle is charging, this endpoint returns the date and time the vehicle expects to complete this charging session. When the vehicle is not charging, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_charge_time('suscipit')

if res.charge_time is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaChargeTimeResponse](../../models/operations/getteslachargetimeresponse.md)**


## get_compass

__Description__

This endpoint returns the compass heading of a Tesla. The value is in degrees, with 0 degrees being North.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_compass('iure')

if res.compass is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaCompassResponse](../../models/operations/getteslacompassresponse.md)**


## get_exterior_temperature

__Description__

This endpoint returns the exterior temperature of a Tesla, in celsius by default.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_exterior_temperature('magnam')

if res.temperature is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaExteriorTemperatureResponse](../../models/operations/getteslaexteriortemperatureresponse.md)**


## get_interior_temperature

__Description__

This endpoint returns the interior temperature of a Tesla, in celsius by default.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_interior_temperature('debitis')

if res.temperature is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaInteriorTemperatureResponse](../../models/operations/getteslainteriortemperatureresponse.md)**


## get_speedometer

__Description__

This endpoint returns the speed of a Tesla (in kilometers/hour by default or in miles/hour using the sc-unit-system).

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_speedometer('ipsa')

if res.speed is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaSpeedResponse](../../models/operations/getteslaspeedresponse.md)**


## get_voltage

__Description__

When the vehicle is plugged in, this endpoint returns the voltage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_voltage('delectus')

if res.charge_voltage is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaVoltageResponse](../../models/operations/getteslavoltageresponse.md)**


## get_wattmeter

__Description__

When the vehicle is plugged in, this endpoint returns the wattage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.get_wattmeter('tempora')

if res.charge_wattage is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetTeslaWattmeterResponse](../../models/operations/getteslawattmeterresponse.md)**


## set_ammeter

__Description__

When the vehicle is plugged in, this endpoint sets the amperage of the charger measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.tesla.set_ammeter('suscipit', shared.ChargeAmmeter(
    amperage=48,
))

if res.success_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `vehicle_id`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `charge_ammeter`                                                       | [Optional[shared.ChargeAmmeter]](../../models/shared/chargeammeter.md) | :heavy_minus_sign:                                                     | N/A                                                                    |


### Response

**[operations.SetTeslaAmmeterResponse](../../models/operations/setteslaammeterresponse.md)**

