from dataclasses import dataclass, field
from typing import List

from http_engine.domain.models import DataItem


@dataclass
class HttpEngineRequest:
    method: str
    url: str
    wanted_data_items: List[DataItem]
    payload: dict = field(default_factory=lambda: {})
    proxy_pool_enabled: bool = False
    timeout: int = 5
