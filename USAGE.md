<!-- Start SDK Example Usage -->
```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
    vehicle_id="corrupti",
)


req = operations.GetLocationRequest()
    
res = s.vehicles.get_location(req)

if res.location is not None:
    # handle response
```
<!-- End SDK Example Usage -->