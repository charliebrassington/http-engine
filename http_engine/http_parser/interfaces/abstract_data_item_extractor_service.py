from abc import ABC, abstractmethod
from typing import List, Dict, Any

from http_engine.domain.models import DataItem


class AbstractDataItemExtractorService(ABC):
    @abstractmethod
    def _get_top_matches(self, flattened_items: List[dict], data_item: DataItem) -> List[dict]:
        raise NotImplementedError

    @abstractmethod
    def extract_data_item_values(self, parsed_response_items: list, data_items: List[DataItem]) -> Dict[str, Any]:
        raise NotImplementedError
