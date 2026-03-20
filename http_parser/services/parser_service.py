from typing import List

from adapters import HttpResponse
from http_parser.interfaces import AbstractResponseParser, AbstractNestedParser, AbstractParserService


class ParserService(AbstractParserService):
    def __init__(self, response_parsers: List[AbstractResponseParser], nested_parsers: List[AbstractNestedParser]) -> None:
        self._response_parsers = response_parsers
        self._nested_parsers = nested_parsers

    def parse_response(self, http_response: HttpResponse) -> list:
        return [parsed_item for parser in self._response_parsers for parsed_item in parser.parse_response(http_response)]
