from dataclasses import dataclass


@dataclass
class CollectProxiesResponse:
    success: bool
    proxy_count: int
