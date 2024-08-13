import os

# Load from .env file
from dotenv import load_dotenv

load_dotenv('.env')
# Spotify Client Credentials
print(os.getenv('SPOTIPY_CLIENT_ID'))
print(os.getenv('SPOTIPY_CLIENT_SECRET'))
SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# BeatSaver API URL
BEATSAVER_BASE_URL = 'https://api.beatsaver.com/'
