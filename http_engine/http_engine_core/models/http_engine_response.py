from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class HttpEngineResponse:
    success: bool
    data_wanted: Dict[str, Any]
