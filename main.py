﻿from src.Controllers.SpotifyController import SpotifyController
from src.Controllers.BeatSaverController import BeatSaverController
from src.Controllers.TwitchController import TwitchController
from src.Services.PastebinService import PastebinService
from src.Services.RedisService import RedisService
from src.Services.SpotifyService import SpotifyService
from src.Services.BeatSaverService import BeatSaverService
from src.Services.TwitchService import TwitchService


def main():
    print("Choose an option:")
    print("1. Enter Spotify playlist URL")
    print("2. Start Twitch bot")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
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
            beat_saver_controller.search_and_download_beginner_maps()

    elif choice == "2":
        redis_service = RedisService()
        beat_saver_service = BeatSaverService(redis_service)
        pastebin_service = PastebinService()
        twitch_service = TwitchService(beat_saver_service, pastebin_service, redis_service)
        twitch_controller = TwitchController(twitch_service)
        twitch_controller.run()

    else:
        print("Invalid choice")
        exit(1)


if __name__ == "__main__":
    main()
