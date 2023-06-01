# webhooks

### Available Operations

* [subscribe](#subscribe) - Subscribe Webhook
* [unsubscribe](#unsubscribe) - Unsubscribe Webhook

## subscribe

__Description__

Subscribe to a webhook for a vehicle.

__Permission__

`required: webhook:read`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|

### Example Usage

```python
import smartcar
from smartcar.models import operations, shared

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.webhooks.subscribe('repellendus', 'sapiente', shared.WebhookInfo(
    vehicleid='dc6ea99e-57d1-4e41-b129-27e7eb58713e',
    webhookid='9b6ae692-60cc-4b3e-89d8-71e7549cf805',
))

if res.success_response is not None:
    # handle response
```

## unsubscribe

__Description__

Delete a webhook for a vehicle.

__Permission__

`required: webhook:read`

__Response body__

|  Name 	|Type   	|Boolean   	|
|---	|---	|---	|
|  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|

### Example Usage

```python
import smartcar
from smartcar.models import operations

s = smartcar.Smartcar(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)


res = s.webhooks.unsubscribe('quo', 'odit')

if res.success_response is not None:
    # handle response
```
