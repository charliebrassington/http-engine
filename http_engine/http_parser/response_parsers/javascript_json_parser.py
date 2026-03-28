import json

from http_engine.adapters import HttpResponse
from http_engine.http_parser.interfaces import AbstractResponseParser


class JavascriptJsonParser(AbstractResponseParser):
    def parse_response(self, http_response: HttpResponse) -> list:
        json_list = []
        for element in http_response.soup.find_all("script"):
            script_text = element.text
            parsed_json = script_text[script_text.find("{"):][:script_text.rfind("}") + 1]
            if len(parsed_json) < 3:
                continue

            try:
                json_list.append(json.loads(parsed_json))

            except json.JSONDecodeError:
                continue

        return json_list
