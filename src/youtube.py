import os
import requests


class YouTubeApi:
    def __init__(self):
        self.api_key = os.environ.get("YouTubeApiKey")
        
    def get_video_by_keyword(self, keyword: str) -> dict:
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={keyword}&type=video&key={self.api_key}"
        response = requests.get(url=url)
        return response.json()