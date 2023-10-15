import os

from src.youtube import YouTubeApi


def test_class_exists():
    assert YouTubeApi
    
def test_class_attributes():
    tube = YouTubeApi()
    assert tube.api_key
    
def test_get_video_by_keyword(keyword):
    tube = YouTubeApi()
    response = tube.get_video_by_keyword(keyword=keyword)
    assert response["items"][0]["id"]["videoId"] == "Nq0djQjBk4M"
    
    
    