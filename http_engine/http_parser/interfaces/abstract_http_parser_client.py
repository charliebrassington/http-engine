from abc import ABC, abstractmethod
from typing import List

from http_engine.domain.models import DataItem
from http_engine.adapters import HttpResponse


class AbstractHttpParserClient(ABC):
    @abstractmethod
    def parse_response(self, response: HttpResponse, data_items: List[DataItem]):
        raise NotImplementedError
