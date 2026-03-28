from abc import ABC, abstractmethod
from typing import Any, Dict


class AbstractFlattenerService(ABC):
    @abstractmethod
    def flatten_object(self, item: Any) -> list:
        raise NotImplementedError

