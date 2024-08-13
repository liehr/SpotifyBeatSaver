from dataclasses import dataclass


@dataclass
class MapStats:
    plays: int
    downloads: int
    upvotes: int
    downvotes: int
    # Add other fields as necessary
    rating: float = None

    def calculate_rating(self):
        return (self.upvotes / + self.downvotes) * 100.0 if self.upvotes + self.downvotes > 0 else 0
