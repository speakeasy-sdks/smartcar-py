"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from smartcar import utils
from smartcar._hooks import HookContext
from smartcar.models import errors, operations, shared
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
        hook_ctx = HookContext(operation_id='subscribe', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.SubscribeRequest(
            vehicle_id=vehicle_id,
            webhook_id=webhook_id,
            webhook_info=webhook_info,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.SubscribeRequest, base_url, '/vehicles/{vehicle_id}/webhooks/{webhookId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.SubscribeRequest, "webhook_info", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.SubscribeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

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
        hook_ctx = HookContext(operation_id='unsubscribe', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.UnsubscribeRequest(
            vehicle_id=vehicle_id,
            webhook_id=webhook_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UnsubscribeRequest, base_url, '/vehicles/{vehicle_id}/webhooks/{webhookId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('DELETE', url, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.UnsubscribeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SuccessResponse])
                res.success_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    