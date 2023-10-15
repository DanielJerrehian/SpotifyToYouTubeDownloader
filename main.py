from math import ceil
from dotenv import load_dotenv

from src.spotify import SpotifyApi
from src.youtube import YouTubeApi
from src.downloader import YouTubeMp3Downloader


def main(playlist_id: str):
    load_dotenv()
    
    spot = SpotifyApi()
    song_count = spot.get_playlist(playlist_id=playlist_id)["tracks"]["total"]
    iterations = ceil(song_count / 50)
    offset = 0
    
    titles = []
    for iteration in range(0, iterations):
        playlist = spot.get_playlist_items(playlist_id=playlist_id, limit=50, offset=offset)
        for track in playlist.get("items", []):
            name = track["track"]["name"]
            artists = [artist["name"] for artist in track["track"]["artists"]]
            titles.append(f"{', '.join(artists)} - {name} - Audio")
        offset = offset + 50
    
    tube = YouTubeApi()
    downloader = YouTubeMp3Downloader()

    urls = []
    for title in titles:
        video  = tube.get_video_by_keyword(keyword=title)
        try:
            url = f'https://www.youtube.com/watch?v={video["items"][0]["id"]["videoId"]}'
            urls.append(url)
        except KeyError:
            pass
    
    for url in urls:
        downloader.download(url=url)
        

main(playlist_id="2tUQNiBZ8Xp5jMfM2T7kvx")