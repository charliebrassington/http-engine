from typing import Any

from http_parser.interfaces import AbstractFlattenerService


class FlattenerService(AbstractFlattenerService):
    def flatten_object(self, item: Any) -> list:
        flattened_object_list = []
        if isinstance(item, dict):
            flattened_object_list.append(item)
            keys_to_check = [k for k, v in item.items() if isinstance(v, (list, dict))]
            flattened_object_list.extend(flattened_obj for key in keys_to_check for flattened_obj in self.flatten_object(item.pop(key)))

        elif isinstance(item, list):
            flattened_object_list.extend(flattened_obj for inner_item in item for flattened_obj in self.flatten_object(inner_item))

        return [obj for obj in flattened_object_list if obj]
