from abc import ABC, abstractmethod

from adapters import HttpResponse


class AbstractParserService(ABC):
    @abstractmethod
    def parse_response(self, http_response: HttpResponse) -> list:
        raise NotImplementedError
