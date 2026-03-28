from abc import ABC, abstractmethod

from http_engine.adapters.models import HttpResponse


class AbstractHttpAdapter(ABC):
    @abstractmethod
    def make_request(self, method: str, url: str, **kwargs) -> HttpResponse:
        raise NotImplementedError
