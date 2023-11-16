"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .cadillac import Cadillac
from .chevrolet import Chevrolet
from .compatibility import Compatibility
from .evs import Evs
from .sdkconfiguration import SDKConfiguration
from .tesla import Tesla
from .user import User
from .vehicle_management import VehicleManagement
from .vehicles import Vehicles
from .webhooks import Webhooks
from smartcar import utils
from smartcar.models import shared
from typing import Callable, Dict, Union

class Smartcar:
    r"""Smartcar API: OpenAPI schema for Smartcar's API"""
    compatibility: Compatibility
    r"""Operations about compatibility"""
    vehicle_management: VehicleManagement
    user: User
    vehicles: Vehicles
    r"""Operations about vehicles"""
    tesla: Tesla
    evs: Evs
    r"""Operations about electric vehicles"""
    cadillac: Cadillac
    chevrolet: Chevrolet
    webhooks: Webhooks

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.compatibility = Compatibility(self.sdk_configuration)
        self.vehicle_management = VehicleManagement(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.vehicles = Vehicles(self.sdk_configuration)
        self.tesla = Tesla(self.sdk_configuration)
        self.evs = Evs(self.sdk_configuration)
        self.cadillac = Cadillac(self.sdk_configuration)
        self.chevrolet = Chevrolet(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
    