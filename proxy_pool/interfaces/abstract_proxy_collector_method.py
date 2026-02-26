from abc import ABC, abstractmethod
from typing import List


class AbstractProxyCollectorMethod:
    @abstractmethod
    def collect_proxies(self, proxy_path: str) -> List[str]:
        raise NotImplementedError
