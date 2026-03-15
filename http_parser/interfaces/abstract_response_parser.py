from abc import ABC, abstractmethod
from typing import Any

from adapters import HttpResponse


class AbstractResponseParser(ABC):
    @abstractmethod
    def parse_response(self, http_response: HttpResponse) -> list:
        raise NotImplementedError

