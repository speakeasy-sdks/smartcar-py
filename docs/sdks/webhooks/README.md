# Webhooks
(*webhooks*)

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
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.webhooks.subscribe(vehicle_id='string', webhook_id='string', webhook_info=shared.WebhookInfo(
    vehicleid='dc6ea99e-57d1-4e41-b129-27e7eb58713e',
    webhookid='9b6ae692-60cc-4b3e-89d8-71e7549cf805',
))

if res.success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `vehicle_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `webhook_id`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `webhook_info`                                                     | [Optional[shared.WebhookInfo]](../../models/shared/webhookinfo.md) | :heavy_minus_sign:                                                 | N/A                                                                |


### Response

**[operations.SubscribeResponse](../../models/operations/subscriberesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
from smartcar.models import shared

s = smartcar.Smartcar(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.webhooks.unsubscribe(vehicle_id='string', webhook_id='string')

if res.success_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `vehicle_id`       | *str*              | :heavy_check_mark: | N/A                |
| `webhook_id`       | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.UnsubscribeResponse](../../models/operations/unsubscriberesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
