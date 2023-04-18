<!-- Start SDK Example Usage -->
```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetLocationRequest(
    vehicle_id="36ab27d0-fd9d-4455-823a-ce30af709ffc",
)
    
res = s.vehicles.get_location(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->