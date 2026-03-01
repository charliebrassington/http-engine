from abc import ABC, abstractmethod
from typing import Callable

from adapters.models import HttpResponse
from http_engine.models import HttpEngineRequest


class AbstractHttpRequestService(ABC):
    @abstractmethod
    def send_http_request(self, engine_request: HttpEngineRequest) -> HttpResponse:
        raise NotImplementedError
