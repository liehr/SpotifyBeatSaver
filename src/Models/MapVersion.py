from dataclasses import dataclass


@dataclass
class MapVersion:
    version: str
    hash: str
    state: str
    # Add other fields as necessary
