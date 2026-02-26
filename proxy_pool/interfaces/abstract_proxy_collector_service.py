from abc import ABC, abstractmethod
from typing import List

from domain.models import ProxyPoolConfig


class AbstractProxyCollectorService(ABC):
    @abstractmethod
    def collect_proxies(self, config: ProxyPoolConfig) -> List[str]:
        raise NotImplementedError
