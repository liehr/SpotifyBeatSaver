import os

# Load from .env file
from dotenv import load_dotenv

load_dotenv('.env')
# Spotify Client Credentials
print(os.getenv('SPOTIPY_CLIENT_ID'))
print(os.getenv('SPOTIPY_CLIENT_SECRET'))
SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# Twitch Client Credentials
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN')
TWITCH_REFRESH_TOKEN = os.getenv('TWITCH_REFRESH_TOKEN')

# Pastebin API Key
PASTEBIN_API_KEY = os.getenv('PASTEBIN_API_KEY')

# BeatSaver API URL
BEATSAVER_BASE_URL = 'https://api.beatsaver.com/'
