from typing import Any

from http_parser.interfaces import AbstractObjectMatcherService
from domain.models import DataItem
from core.fuzzy_string_matcher import match_strings_ratio


class ObjectMatcherService(AbstractObjectMatcherService):
    def get_match_count_for_object(self, target_obj: dict, data_item: DataItem) -> int:
        return sum(
            result
            for k, v in target_obj.items()
            for keyword in data_item.keywords
            for check_item in (k, v)
            if (result := match_strings_ratio(str(check_item), keyword)) > 50
        )

    def get_match_value(self, target_obj: dict, data_item: DataItem) -> Any:
        key_match_values = [
            (max(match_strings_ratio(k, keyword) for keyword in data_item.keywords), k)
            for k in target_obj
        ]

        top_key_match = sorted(key_match_values, key=lambda x: x[0], reverse=True)[0][1]
        return target_obj[top_key_match]
