from dataclasses import dataclass
from typing import List, Optional

from src.Models.UserDetail import UserDetail
from src.Models.MapDetailMetadata import MapDetailMetadata
from src.Models.MapStats import MapStats
from src.Models.MapVersion import MapVersion


@dataclass
class MapDetail:
    automapper: bool
    blQualified: bool
    blRanked: bool
    bookmarked: bool
    createdAt: str
    declaredAi: str
    description: str
    id: str
    metadata: MapDetailMetadata
    name: str
    qualified: bool
    ranked: bool
    stats: MapStats
    updatedAt: str
    uploaded: str
    uploader: UserDetail
    versions: List[MapVersion]
    collaborators: Optional[List[UserDetail]] = None
    curatedAt: Optional[str] = None
    curator: Optional[UserDetail] = None
    deletedAt: Optional[str] = None
    lastPublishedAt: Optional[str] = None
    tags: Optional[List[str]] = None

    def filter_info(self):
        return {
            "metadata": self.metadata,
            "downloadLink": f"https://api.beatsaver.com/download/{self.id}",
            "stats": self.stats,
            "versions": self.versions
        }
