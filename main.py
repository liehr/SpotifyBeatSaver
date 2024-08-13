from src.Controllers.SpotifyController import SpotifyController
from src.Controllers.BeatSaverController import BeatSaverController
from src.Services.SpotifyService import SpotifyService
from src.Services.BeatSaverService import BeatSaverService

if __name__ == "__main__":
    playlist_url = input("Enter Spotify playlist URL: ")

    # Check if the playlist URL is valid spotify playlist url
    # Scheme: https://open.spotify.com/playlist/{playlist_id}

    if not playlist_url.startswith("https://open.spotify.com/playlist/"):
        print("Invalid Spotify playlist URL")
        exit(1)

    spotify_service = SpotifyService()
    spotify_controller = SpotifyController(spotify_service)
    beat_saver_service = BeatSaverService()
    beat_saver_controller = BeatSaverController(beat_saver_service)

    for song in spotify_controller.get_playlist_tracks(playlist_url):
        print(f"Searching for {song}...")
        beat_saver_controller.search_and_download(song)
