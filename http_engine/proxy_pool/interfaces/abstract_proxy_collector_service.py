from abc import ABC, abstractmethod
from typing import List

from http_engine.domain.models import ProxyPoolConfig


class AbstractProxyCollectorService(ABC):
    @abstractmethod
    def collect_proxies(self, config: ProxyPoolConfig) -> List[str]:
        raise NotImplementedError
