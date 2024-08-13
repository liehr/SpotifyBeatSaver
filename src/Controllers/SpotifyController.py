from src.Services.SpotifyService import SpotifyService


class SpotifyController:
    def __init__(self, spotify_service: SpotifyService):
        self.spotify_service = spotify_service

    def get_playlist_tracks(self, playlist_url: str):
        return self.spotify_service.get_playlist_tracks(playlist_url)
