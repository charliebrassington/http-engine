import json

from dataclasses import dataclass
from typing import Any

from bs4 import BeautifulSoup


@dataclass
class HttpResponse:
    raw_text: str
    status_code: int

    @property
    def json(self) -> Any:
        return json.loads(self.raw_text)

    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.raw_text)
