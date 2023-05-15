"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .cadillac import Cadillac
from .chevrolet import Chevrolet
from .compatibility import Compatibility
from .evs import Evs
from .tesla import Tesla
from .user import User
from .vehicles import Vehicles
from .webhooks import Webhooks
from smartcar.models import shared

SERVERS = [
    "https://api.smartcar.com/v2.0",
    r"""Smartcar API"""
]
"""Contains the list of servers available to the SDK"""

class Smartcar:
    r"""# How do I use Postman with Smartcar?
    We've detailed how to get started with Smartcar in Postman [here](https://www.notion.so/smartcarapi/How-do-I-use-Postman-with-Smartcar-b8e8483bae8b43a986715582beb54bd4).
    """
    cadillac: Cadillac
    chevrolet: Chevrolet
    compatibility: Compatibility
    r"""Operations about compatibility"""
    evs: Evs
    r"""Operations about electric vehicles"""
    tesla: Tesla
    user: User
    vehicles: Vehicles
    r"""Operations about vehicles"""
    webhooks: Webhooks

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "3.3.0"
    _gen_version: str = "2.27.0"

    def __init__(self,
                 security: shared.Security = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = utils.configure_security_client(self._client, security)
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.cadillac = Cadillac(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.chevrolet = Chevrolet(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.compatibility = Compatibility(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.evs = Evs(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.tesla = Tesla(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user = User(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.vehicles = Vehicles(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    