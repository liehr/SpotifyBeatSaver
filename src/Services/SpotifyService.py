import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from src.Utils.SpotifyUtils import extract_playlist_id
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET


class SpotifyService:
    def __init__(self, client_credentials_manager=None):
        if client_credentials_manager is None:
            client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                                  client_secret=SPOTIPY_CLIENT_SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_playlist_tracks(self, playlist_url: str):
        playlist_id = extract_playlist_id(playlist_url)
        song_names = []
        offset = 0
        limit = 100

        while True:
            response = self.sp.playlist_items(playlist_id, offset=offset, limit=limit)
            items = response['items']

            if not items:
                break

            for item in items:
                song_names.append(item['track']['name'] + ' ' + item['track']['artists'][0]['name'])

            offset += limit

        return song_names
