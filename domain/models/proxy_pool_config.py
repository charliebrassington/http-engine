from dataclasses import dataclass

from domain.models.proxy_type import ProxyType


@dataclass
class ProxyPoolConfig:
    timeout: int = 5
    ratelimit: int = 300
    proxy_type: ProxyType = ProxyType.FREE
    proxy_path: str = ""
    dead_proxy_fail_limit: int = 100
