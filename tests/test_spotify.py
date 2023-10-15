import os

from src.spotify import SpotifyApi


def test_class_exists():
    assert SpotifyApi
    
def test_class_attributes():
    spot = SpotifyApi()
    assert spot.client_id
    assert spot.client_secret
    assert spot.token
    
def test_get_playlist(playlist_id):
    spot = SpotifyApi()
    response = spot.get_playlist(playlist_id=playlist_id)
    assert len(response.get("tracks", [])) >= 1
    
def test_get_playlist_items(playlist_id):
    spot = SpotifyApi()
    response = spot.get_playlist_items(playlist_id=playlist_id, limit=1)
    assert len(response.get("items", [])) == 1
    
    