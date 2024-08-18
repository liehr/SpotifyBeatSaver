from src.Services.BeatSaverService import BeatSaverService
from src.Models.SearchParams import SearchParams


class BeatSaverController:
    def __init__(self, beat_saver_service: BeatSaverService):
        self.beat_saver_service = beat_saver_service

    def search_and_download_with_query(self, search_query: str):
        search_params = SearchParams(q=search_query, sortOrder="Relevance", leaderboard="All")
        return self.beat_saver_service.search_text(page=0, params=search_params)

    def search_and_download_beginner_maps(self):
        search_params = SearchParams(sortOrder="Relevance", leaderboard="All", minNps=0.8, maxNps=3.0)
        return self.beat_saver_service.search_text(page=0, params=search_params)
