<!-- Start SDK Example Usage [usage] -->
```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.vehicles.get_location(vehicle_id='36ab27d0-fd9d-4455-823a-ce30af709ffc')

if res.location is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->