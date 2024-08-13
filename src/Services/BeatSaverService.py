import os
import re
import requests
import zipfile
from src.Models.MapDetail import MapDetail
from src.Models.SearchParams import SearchParams
from src.Models.SearchResponse import SearchResponse
from config import BEATSAVER_BASE_URL


class BeatSaverService:
    def __init__(self, http_client=None):
        if http_client is None:
            http_client = requests
        self.http_client = http_client

    def _get(self, endpoint: str, params: dict = None):
        url = f"{BEATSAVER_BASE_URL}/{endpoint}"
        response = self.http_client.get(url, params=params)
        return self._handle_response(response)

    @staticmethod
    def _handle_response(response: requests.Response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def download_zip(download_link: str, file_name: str, search_query: str):
        search_query = re.sub(r'[^A-Za-z0-9 ]+', '', search_query)
        search_query = search_query.replace(" ", "_")

        file_name = re.sub(r'[^A-Za-z0-9. ]+', '', file_name)
        file_name = file_name.replace(" ", "_")

        folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "BeatSaver_Spotify", search_query)

        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        print(file_path)

        response = requests.get(download_link)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)

            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                extract_folder = os.path.join(folder_path, file_name.replace('.zip', ''))
                os.makedirs(extract_folder, exist_ok=True)
                zip_ref.extractall(extract_folder)

            os.remove(file_path)
        else:
            response.raise_for_status()

    def search_text(self, page: int, params: SearchParams) -> SearchResponse:
        endpoint = f"search/text/{page}"
        params_dict = {k: v for k, v in params.__dict__.items() if v is not None}
        response_json = self._get(endpoint, params=params_dict)
        search_response = self._map_to_search_response(response_json)
        search_response.docs = [doc.filter_info() for doc in search_response.docs]

        for i, doc in enumerate(search_response.docs[:5]):
            download_link = doc["versions"][0]["downloadURL"]
            song_name = doc["metadata"]["songName"]
            song_author = doc["metadata"]["songAuthorName"]

            song_name = re.sub(r'[^A-Za-z0-9 ]+', '', song_name)
            song_author = re.sub(r'[^A-Za-z0-9 ]+', '', song_author)

            file_name = f"map_{song_name}_{song_author}.zip"
            self.download_zip(download_link, file_name, params.q)

        return search_response

    @staticmethod
    def _map_to_search_response(data: dict) -> SearchResponse:
        docs = [MapDetail(**doc) for doc in data.get('docs', [])]
        redirect = data.get('redirect')
        return SearchResponse(docs=docs, redirect=redirect)
