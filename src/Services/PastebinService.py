import requests
from config import PASTEBIN_API_KEY


class PastebinService:
    def __init__(self):
        self.api_key = PASTEBIN_API_KEY
        self.api_url = "https://pastebin.com/api/api_post.php"

    def create_paste(self, title, content):
        data = {
            'api_dev_key': self.api_key,
            'api_option': 'paste',
            'api_paste_code': content,
            'api_paste_name': title,
            'api_paste_private': 1,  # 0=public, 1=unlisted, 2=private
            'api_paste_expire_date': 'N'
        }

        response = requests.post(self.api_url, data=data)

        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Failed to create paste")
