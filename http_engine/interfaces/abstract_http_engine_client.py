from abc import ABC, abstractmethod

from http_engine.models import HttpEngineRequest, HttpEngineResponse


class AbstractHttpEngineClient(ABC):
    @abstractmethod
    def send_http_request(self, http_request: HttpEngineRequest) -> HttpEngineResponse:
        raise NotImplementedError
