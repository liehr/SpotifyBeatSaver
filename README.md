# BeatSaver Spotify Integration 🎵

This project integrates Spotify playlists with BeatSaver, allowing you to download Beat Saber maps based on your favorite Spotify tracks.

## Features ✨
- Extracts tracks from a Spotify playlist
- Searches for corresponding Beat Saber maps on BeatSaver
- Downloads and unzips the maps into organized folders

## Prerequisites 📋
- Spotify Developer Account and created application
- Python 3.7+
- pip (Python package installer)

## Setup 🛠️

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/beatsaver-spotify-integration.git
    cd beatsaver-spotify-integration
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory with the following content:**
    ```dotenv
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    ```

    Replace `your_spotify_client_id` and `your_spotify_client_secret` with your actual Spotify API credentials.

## Usage 🚀

1. **Run the main script:**
    ```sh
    python main.py
    ```

2. **Enter the Spotify playlist URL when prompted.**

The script will search for Beat Saber maps corresponding to the tracks in the playlist and download them to your desktop.

## License 📄
This project is licensed under the MIT License.
