from abc import ABC, abstractmethod
from typing import List

from domain.models import DataItem
from adapters import HttpResponse


class AbstractHttpParserClient(ABC):
    @abstractmethod
    def parse_response(self, response: HttpResponse, data_items: List[DataItem]):
        raise NotImplementedError
