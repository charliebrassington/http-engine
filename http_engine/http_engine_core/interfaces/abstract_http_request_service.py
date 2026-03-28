from abc import ABC, abstractmethod
from typing import Callable

from http_engine.adapters.models import HttpResponse
from http_engine.http_engine_core.models import HttpEngineRequest


class AbstractHttpRequestService(ABC):
    @abstractmethod
    def send_http_request(self, engine_request: HttpEngineRequest) -> HttpResponse:
        raise NotImplementedError
