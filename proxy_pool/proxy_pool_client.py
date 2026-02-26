from domain.models import ProxyPoolConfig, ProxyType

from proxy_pool.interfaces import AbstractProxyPoolClient, AbstractProxyCollectorService
from proxy_pool.models import CollectProxiesResponse
from proxy_pool.errors import ProxyPathNotSet


class ProxyPoolClient(AbstractProxyPoolClient):
    def __init__(self, proxy_collector_service: AbstractProxyCollectorService) -> None:
        self._proxy_collector_service = proxy_collector_service

        self._config = ProxyPoolConfig()
        self._proxies = []

    def set_config(self, config: ProxyPoolConfig) -> None:
        self._config = config

    def collect_proxies(self) -> CollectProxiesResponse:
        self._proxies = self._proxy_collector_service.collect_proxies(self._config)

        return CollectProxiesResponse(success=True, proxy_count=len(self._proxies))
