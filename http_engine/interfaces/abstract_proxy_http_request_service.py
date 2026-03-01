from abc import ABC, abstractmethod

from http_engine.models import HttpEngineRequest
from adapters import HttpResponse


class AbstractProxyHttpRequestService(ABC):
    @abstractmethod
    def send_proxied_http_request(self, engine_request: HttpEngineRequest) -> HttpResponse:
        raise NotImplementedError

