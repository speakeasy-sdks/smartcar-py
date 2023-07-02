# user

### Available Operations

* [get_info](#get_info) - User Info

## get_info

__Description__

Returns the id of the vehicle owner who granted access to your application. This should be used as the static unique identifier for storing the access token and refresh token pair in your database. Note: A single user can own multiple vehicles, and multiple users can own the same vehicle.

### Example Usage

```python
import smartcar


s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.user.get_info()

if res.user_info is not None:
    # handle response
```


### Response

**[operations.GetInfoResponse](../../models/operations/getinforesponse.md)**

