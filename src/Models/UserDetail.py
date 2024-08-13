from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDetail:
    id: str
    name: str
    avatar: Optional[str] = None
    # Add other fields as necessary
