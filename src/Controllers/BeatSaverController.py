from src.Services.BeatSaverService import BeatSaverService
from src.Models.SearchParams import SearchParams


class BeatSaverController:
    def __init__(self, beat_saver_service: BeatSaverService):
        self.beat_saver_service = beat_saver_service

    def search_and_download(self, search_query: str):
        search_params = SearchParams(q=search_query, sortOrder="Rating", leaderboard="All")
        return self.beat_saver_service.search_text(page=0, params=search_params)
