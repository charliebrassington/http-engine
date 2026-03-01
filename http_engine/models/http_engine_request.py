from dataclasses import dataclass, field
from typing import List


@dataclass
class HttpEngineRequest:
    method: str
    url: str
    wanted_data_keys: List[str]
    payload: dict = field(default_factory=lambda: {})
    proxy_pool_enabled: bool = False
