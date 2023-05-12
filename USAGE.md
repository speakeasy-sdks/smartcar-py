<!-- Start SDK Example Usage -->
```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.vehicles.get_location('36ab27d0-fd9d-4455-823a-ce30af709ffc')

if res.location is not None:
    # handle response
```
<!-- End SDK Example Usage -->