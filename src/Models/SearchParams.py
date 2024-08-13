from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchParams:
    automapper: Optional[bool] = None
    chroma: Optional[bool] = None
    cinema: Optional[bool] = None
    curated: Optional[bool] = None
    followed: Optional[bool] = None
    from_date: Optional[str] = None
    fullSpread: Optional[bool] = None
    leaderboard: str = "All"
    maxBpm: Optional[float] = None
    maxDuration: Optional[int] = None
    maxNps: Optional[float] = None
    maxRating: Optional[float] = None
    me: Optional[bool] = None
    minBpm: Optional[float] = None
    minDuration: Optional[int] = None
    minNps: Optional[float] = None
    minRating: Optional[float] = None
    noodle: Optional[bool] = None
    q: Optional[str] = None
    sortOrder: str = "Latest"
    tags: Optional[str] = None
    to_date: Optional[str] = None
    verified: Optional[bool] = None
