from typing import List, Dict, Any

from http_engine.domain.models import DataItem
from http_engine.http_parser.interfaces import AbstractDataItemExtractorService, AbstractObjectMatcherService, AbstractFlattenerService


class DataItemExtractorService(AbstractDataItemExtractorService):
    def __init__(self, object_matcher_service: AbstractObjectMatcherService, flattener_service: AbstractFlattenerService) -> None:
        self._object_matcher_service = object_matcher_service
        self._flattener_service = flattener_service

    def _get_top_matches(self, flattened_items: List[dict], data_item: DataItem) -> List[dict]:
        data_match_count = [
            (self._object_matcher_service.get_match_count_for_object(flattened_item, data_item), flattened_item)
            for flattened_item in flattened_items
        ]

        sorted_data_match_count = sorted(data_match_count, key=lambda x: x[0], reverse=True)
        top_match_count = sorted_data_match_count[0][0]

        return [flattened_item for match_count, flattened_item in sorted_data_match_count if match_count == top_match_count]

    def extract_data_item_values(self, parsed_response_items: list, data_items: List[DataItem]) -> Dict[str, Any]:
        flattened_items = [flattened_item for item in parsed_response_items for flattened_item in self._flattener_service.flatten_object(item)]

        data_item_values = {
            data_item.name: self._object_matcher_service.get_match_value(item, data_item)
            for data_item in data_items
            for item in self._get_top_matches(flattened_items, data_item)
        }

        return data_item_values
