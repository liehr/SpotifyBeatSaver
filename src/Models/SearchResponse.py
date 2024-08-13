from dataclasses import dataclass
from typing import List, Optional

from src.Models.MapDetail import MapDetail


@dataclass
class SearchResponse:
    docs: List[MapDetail]
    redirect: Optional[str]
