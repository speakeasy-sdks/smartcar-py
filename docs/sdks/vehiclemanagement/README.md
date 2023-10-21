# VehicleManagement
(*vehicle_management*)

### Available Operations

* [delete_management_vehicle_connections](#delete_management_vehicle_connections) - Delete vehicle connections by user_id or vehicle_id
* [get_management_vehicle_connections](#get_management_vehicle_connections) - Retrieve vehicle connections

## delete_management_vehicle_connections

Delete all connections by vehicle or user ID.

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar()


res = s.vehicle_management.delete_management_vehicle_connections(operations.DeleteManagementVehicleConnectionsSecurity(
    password="",
    username="",
), user_id='string', vehicle_id='string')

if res.deleted_connections_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                     | [operations.DeleteManagementVehicleConnectionsSecurity](../../models/operations/deletemanagementvehicleconnectionssecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |
| `user_id`                                                                                                                      | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Delete all connections containing this user ID (UUID v4).                                                                      |
| `vehicle_id`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | Delete all connections containing this vehicle ID (UUID v4).                                                                   |
| `server_url`                                                                                                                   | *Optional[str]*                                                                                                                | :heavy_minus_sign:                                                                                                             | An optional server URL to use.                                                                                                 |


### Response

**[operations.DeleteManagementVehicleConnectionsResponse](../../models/operations/deletemanagementvehicleconnectionsresponse.md)**


## get_management_vehicle_connections

Returns a paged list of all the vehicles that are connected to the application associated with the management API token used sorted in descending order by connection date.

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar()


res = s.vehicle_management.get_management_vehicle_connections(operations.GetManagementVehicleConnectionsSecurity(
    password="",
    username="",
), cursor=311286, limit=688212, user_id='string', vehicle_id='string')

if res.connections_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                   | [operations.GetManagementVehicleConnectionsSecurity](../../models/operations/getmanagementvehicleconnectionssecurity.md)                     | :heavy_check_mark:                                                                                                                           | The security requirements to use for the request.                                                                                            |
| `cursor`                                                                                                                                     | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Used for accessing pages other than the first page. Each page returned has a cursor value that can be passed here to fetch the “next” page.  |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Number of connections to return (default: 10, maximum: 100).                                                                                 |
| `user_id`                                                                                                                                    | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Filter for connections created by the provider user ID.                                                                                      |
| `vehicle_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Filter for connections to the provided vehicle ID.                                                                                           |
| `server_url`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | An optional server URL to use.                                                                                                               |


### Response

**[operations.GetManagementVehicleConnectionsResponse](../../models/operations/getmanagementvehicleconnectionsresponse.md)**

