import os
import requests


class SpotifyApi:
    def __init__(self):
        self.client_id = os.environ.get("SpotifyClientId")
        self.client_secret = os.environ.get("SpotifyClientSecret")
        self.token = self._get_token().get("access_token")
    
    def _get_token(self):
        url = "https://accounts.spotify.com/api/token"
        body = {"client_id": self.client_id, "client_secret": self.client_secret, "grant_type": "client_credentials"}
        response = requests.post(url=url, data=body)
        return response.json()
    
    def get_playlist(self, playlist_id: str) -> dict:
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url=url, headers=headers)
        return response.json()
    
    def get_playlist_items(self, playlist_id: str, limit: int = 20, offset: int = 0) -> dict:
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={limit}&offset={offset}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url=url, headers=headers)
        return response.json()