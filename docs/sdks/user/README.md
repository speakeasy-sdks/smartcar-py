# User
(*user*)

### Available Operations

* [get_info](#get_info) - User Info

## get_info

__Description__

Returns the id of the vehicle owner who granted access to your application. This should be used as the static unique identifier for storing the access token and refresh token pair in your database. Note: A single user can own multiple vehicles, and multiple users can own the same vehicle.

### Example Usage

```python
import smartcar
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.user.get_info()

if res.user_info is not None:
    # handle response
    pass
```


### Response

**[operations.GetInfoResponse](../../models/operations/getinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
