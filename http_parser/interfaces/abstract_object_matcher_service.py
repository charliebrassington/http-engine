from abc import ABC, abstractmethod
from typing import Any

from domain.models import DataItem


class AbstractObjectMatcherService(ABC):
    @abstractmethod
    def get_match_count_for_object(self, target_obj: dict, data_item: DataItem) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_match_value(self, target_obj: dict, data_item: DataItem) -> Any:
        raise NotImplementedError
