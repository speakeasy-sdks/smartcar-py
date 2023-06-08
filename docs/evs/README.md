# evs

## Overview

Operations about electric vehicles

### Available Operations

* [get_battery_capacity](#get_battery_capacity) - EV Battery Capacity
* [get_battery_level](#get_battery_level) - EV Battery Level
* [get_charging_limit](#get_charging_limit) - EV Charging Limit
* [get_charging_status](#get_charging_status) - EV Charging Status
* [set_charging_limit](#set_charging_limit) - Set EV Charging Limit
* [start_stop_charge](#start_stop_charge) - Start or stop charging an electric vehicle. Please contact us to request early access.

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
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.evs.get_battery_capacity('unde')

if res.battery_capacity is not None:
    # handle response
```

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
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.evs.get_battery_level('nulla')

if res.battery_level is not None:
    # handle response
```

## get_charging_limit

__Description__

Returns the current charge limit of an electric vehicle.

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.evs.get_charging_limit('corrupti')

if res.charge_limit is not None:
    # handle response
```

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
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.evs.get_charging_status('illum')

if res.charge_status is not None:
    # handle response
```

## set_charging_limit

__Description__

Returns the current charge limit of an electric vehicle.

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.evs.set_charging_limit('vel', shared.ChargeLimit(
    limit=1,
))

if res.success_response is not None:
    # handle response
```

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
        bearer_auth="",
    ),
)


res = s.evs.start_stop_charge('error', shared.ChargeAction(
    action=shared.ChargeActionAction.START,
))

if res.success_response is not None:
    # handle response
```
