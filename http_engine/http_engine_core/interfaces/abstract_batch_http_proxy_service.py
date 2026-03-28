from abc import ABC, abstractmethod
from typing import List

from http_engine.adapters import HttpResponse
from http_engine.http_engine_core.models import HttpEngineRequest


class AbstractBatchHttpProxyService(ABC):
    @abstractmethod
    def threaded_proxied_http_request(self, engine_request: HttpEngineRequest, responses: List[HttpResponse]) -> None:
        raise NotImplementedError

    @abstractmethod
    def send_batched_http_request(self, engine_request: HttpEngineRequest, batch_amount: int = 10) -> HttpResponse:
        raise NotImplementedError
