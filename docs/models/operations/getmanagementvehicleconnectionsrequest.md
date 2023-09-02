# GetManagementVehicleConnectionsRequest


## Fields

| Field                                                                                                                                        | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                                                     | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Used for accessing pages other than the first page. Each page returned has a cursor value that can be passed here to fetch the “next” page.  |
| `limit`                                                                                                                                      | *Optional[int]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Number of connections to return (default: 10, maximum: 100).                                                                                 |
| `user_id`                                                                                                                                    | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Filter for connections created by the provider user ID.                                                                                      |
| `vehicle_id`                                                                                                                                 | *Optional[str]*                                                                                                                              | :heavy_minus_sign:                                                                                                                           | Filter for connections to the provided vehicle ID.                                                                                           |