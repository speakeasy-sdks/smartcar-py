"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from smartcar import utils
from smartcar.models import operations, shared
from typing import Optional

class Webhooks:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def subscribe(self, vehicle_id: str, webhook_id: str, webhook_info: Optional[shared.WebhookInfo] = None) -> operations.SubscribeResponse:
        r"""Subscribe Webhook
        __Description__
        
        Subscribe to a webhook for a vehicle.
        
        __Permission__
        
        `required: webhook:read`
        
        __Response body__
        
        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|
        """
        request = operations.SubscribeRequest(
            vehicle_id=vehicle_id,
            webhook_id=webhook_id,
            webhook_info=webhook_info,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.SubscribeRequest, base_url, '/vehicles/{vehicle_id}/webhooks/{webhookId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "webhook_info", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SubscribeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out

        return res

    
    def unsubscribe(self, vehicle_id: str, webhook_id: str) -> operations.UnsubscribeResponse:
        r"""Unsubscribe Webhook
        __Description__
        
        Delete a webhook for a vehicle.
        
        __Permission__
        
        `required: webhook:read`
        
        __Response body__
        
        |  Name 	|Type   	|Boolean   	|
        |---	|---	|---	|
        |  status|   string|  If the request is successful, Smartcar will return “success” (HTTP 200 status).|
        """
        request = operations.UnsubscribeRequest(
            vehicle_id=vehicle_id,
            webhook_id=webhook_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UnsubscribeRequest, base_url, '/vehicles/{vehicle_id}/webhooks/{webhookId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UnsubscribeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out

        return res

    