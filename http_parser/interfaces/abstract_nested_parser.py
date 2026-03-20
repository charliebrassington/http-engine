from abc import ABC, abstractmethod
from typing import Any


class AbstractNestedParser(ABC):
    @abstractmethod
    def parse_response_item(self, item: Any) -> Any:
        raise NotImplementedError

