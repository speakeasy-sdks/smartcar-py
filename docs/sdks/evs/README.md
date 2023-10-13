# Evs
(*evs*)

## Overview

Operations about electric vehicles

### Available Operations

* [get_battery_capacity](#get_battery_capacity) - EV Battery Capacity
* [get_battery_level](#get_battery_level) - EV Battery Level
* [get_charging_limit](#get_charging_limit) - EV Charging Limit
* [get_charging_status](#get_charging_status) - EV Charging Status
* [set_charging_limit](#set_charging_limit) - Set EV Charging Limit
* [start_stop_charge](#start_stop_charge) - Start or stop charging an electric vehicle.

## get_battery_capacity

__Description__

Returns the total capacity of an electric vehicle's battery.

__Permission__

`read_battery`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  capacity|   number|  The total capacity of the vehicle's battery (in kilowatt-hours). 	|

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


res = s.evs.get_battery_capacity(vehicle_id='Crew')

if res.battery_capacity is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetBatteryCapacityResponse](../../models/operations/getbatterycapacityresponse.md)**


## get_battery_level

__Description__

Retrieve EV battery level of a vehicle.

__Permission__

`read_battery`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  `percentRemaining`|   number|  An EV battery’s state of charge (in percent). 	|
|   `range`|   number	|   The estimated remaining distance the vehicle can travel (in kilometers by default or in miles using the [sc-unit-system](https://smartcar.com/docs/api?version=v2.0&language=cURL#request-headers).	|

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


res = s.evs.get_battery_level(vehicle_id='Movies')

if res.battery_level is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetBatteryLevelResponse](../../models/operations/getbatterylevelresponse.md)**


## get_charging_limit

__Description__

Returns the current charge limit of an electric vehicle.

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


res = s.evs.get_charging_limit(vehicle_id='vertical')

if res.charge_limit is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetChargingLimitResponse](../../models/operations/getcharginglimitresponse.md)**


## get_charging_status

__Description__

Returns the current charge status of an electric vehicle.

__Permission__

`read_charge`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  `isPluggedIn` 	|   boolean	|  Indicates whether a charging cable is currently plugged into the vehicle’s charge port. 	|
|   `state`	|   string	|   Indicates whether the vehicle is currently charging. Options: `CHARGING` `FULLY_CHARGED` `NOT_CHARGING`	|

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


res = s.evs.get_charging_status(vehicle_id='Health')

if res.charge_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetChargingStatusResponse](../../models/operations/getchargingstatusresponse.md)**


## set_charging_limit

__Description__

Returns the current charge limit of an electric vehicle.

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


res = s.evs.set_charging_limit(vehicle_id='dynamic', charge_limit=shared.ChargeLimit(
    limit=1,
))

if res.success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `vehicle_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `charge_limit`                                                     | [Optional[shared.ChargeLimit]](../../models/shared/chargelimit.md) | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.SetChargingLimitResponse](../../models/operations/setcharginglimitresponse.md)**


## start_stop_charge

__Description__

Returns the current charge status of an electric vehicle.

__Permission__

`read_charge`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  `isPluggedIn` 	|   boolean	|  Indicates whether a charging cable is currently plugged into the vehicle’s charge port. 	|
|   `state`	|   string	|   Indicates whether the vehicle is currently charging. Options: `CHARGING` `FULLY_CHARGED` `NOT_CHARGING`	|

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


res = s.evs.start_stop_charge(vehicle_id='beside', charge_action=shared.ChargeAction(
    action=shared.ChargeActionAction.START,
))

if res.success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `vehicle_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `charge_action`                                                      | [Optional[shared.ChargeAction]](../../models/shared/chargeaction.md) | :heavy_minus_sign:                                                   | N/A                                                                  |


### Response

**[operations.StartStopChargeResponse](../../models/operations/startstopchargeresponse.md)**

