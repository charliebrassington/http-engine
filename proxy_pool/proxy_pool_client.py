import random

from domain.models import ProxyPoolConfig, ProxyType

from proxy_pool.interfaces import AbstractProxyPoolClient, AbstractProxyCollectorService, AbstractProxyQualityService
from proxy_pool.models import CollectProxiesResponse


class ProxyPoolClient(AbstractProxyPoolClient):
    def __init__(
        self,
        proxy_collector_service: AbstractProxyCollectorService,
        proxy_quality_service: AbstractProxyQualityService
    ) -> None:
        self._proxy_collector_service = proxy_collector_service
        self._proxy_quality_service = proxy_quality_service

        self._config = ProxyPoolConfig()

    def set_config(self, config: ProxyPoolConfig) -> None:
        self._config = config

    def collect_proxies(self) -> CollectProxiesResponse:
        proxies = self._proxy_collector_service.collect_proxies(self._config)
        for proxy in proxies:
            self._proxy_quality_service.update_proxy(proxy=proxy, success=True)

        return CollectProxiesResponse(success=True, proxy_count=len(self._proxy_quality_service.get_proxy_list()))

    def update_proxy_quality(self, proxy: str, success: bool) -> None:
        self._proxy_quality_service.update_proxy(proxy, success)
        self._proxy_quality_service.remove_dead_proxies(dead_proxy_fail_limit=self._config.dead_proxy_fail_limit)

    def get_proxy(self) -> str:
        return random.choice(self._proxy_quality_service.get_proxy_list())
