from abc import ABC, abstractmethod

from domain.models import ProxyPoolConfig
from proxy_pool.models import CollectProxiesResponse


class AbstractProxyPoolClient(ABC):
    @abstractmethod
    def set_config(self, config: ProxyPoolConfig) -> None:
        raise NotImplementedError

    @abstractmethod
    def collect_proxies(self) -> CollectProxiesResponse:
        raise NotImplementedError

    @abstractmethod
    def update_proxy_quality(self, proxy: str, success: bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_proxy(self) -> str:
        raise NotImplementedError
