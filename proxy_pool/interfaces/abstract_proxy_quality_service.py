from abc import ABC, abstractmethod
from typing import List


class AbstractProxyQualityService(ABC):
    @abstractmethod
    def update_proxy(self, proxy: str, success: bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_dead_proxies(self, dead_proxy_fail_limit: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_proxy_list(self) -> List[str]:
        raise NotImplementedError
