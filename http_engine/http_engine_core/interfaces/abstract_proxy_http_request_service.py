from abc import ABC, abstractmethod

from http_engine.http_engine_core.models import HttpEngineRequest
from http_engine.adapters import HttpResponse


class AbstractProxyHttpRequestService(ABC):
    @abstractmethod
    def send_proxied_http_request(self, engine_request: HttpEngineRequest) -> HttpResponse:
        raise NotImplementedError

