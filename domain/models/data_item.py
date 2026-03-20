from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DataItem:
    name: str
    keywords: List[str]
    regex: Optional[str] = None
