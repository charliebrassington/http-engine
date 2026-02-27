from typing import Dict, List
from collections import defaultdict

from proxy_pool.interfaces import AbstractProxyQualityService


class ProxyQualityService(AbstractProxyQualityService):
    def __init__(self) -> None:
        self._proxy_quality_dict: Dict[str, int] = defaultdict(int)
        self._dead_proxies = set()

    def update_proxy(self, proxy: str, success: bool) -> None:
        if proxy not in self._dead_proxies:
            self._proxy_quality_dict[proxy] += 1 if success else -1

    def remove_dead_proxies(self, dead_proxy_fail_limit: int) -> None:
        for k, v in self._proxy_quality_dict.copy().items():
            if v == -dead_proxy_fail_limit:
                self._proxy_quality_dict.pop(k, None)
                self._dead_proxies.add(k)

    def get_proxy_list(self) -> List[str]:
        return list(self._proxy_quality_dict)
