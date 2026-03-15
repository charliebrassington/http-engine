from typing import List

from domain.models import DataItem
from adapters import HttpResponse
from http_parser.interfaces import (
    AbstractHttpParserClient,
    AbstractParserService,
    AbstractDataItemExtractorService,
    AbstractObjectMatcherService
)


class HttpParserClient(AbstractHttpParserClient):
    def __init__(self, parser_service: AbstractParserService, data_item_extractor_service: AbstractDataItemExtractorService) -> None:
        self._parser_service = parser_service
        self._data_item_extractor_service = data_item_extractor_service

    def parse_response(self, response: HttpResponse, data_items: List[DataItem]):
        parsed_result_items = self._parser_service.parse_response(http_response=response)
        return self._data_item_extractor_service.extract_data_item_values(parsed_result_items, data_items)
