from abc import ABC, abstractmethod

from http_engine.http_engine_core.models import HttpEngineRequest, HttpEngineResponse


class AbstractHttpEngineClient(ABC):
    @abstractmethod
    def send_http_request(self, http_request: HttpEngineRequest) -> HttpEngineResponse:
        raise NotImplementedError
