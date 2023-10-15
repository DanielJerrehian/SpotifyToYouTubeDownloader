
from pytube import YouTube, exceptions


class YouTubeMp3Downloader:
    def __init__(self):
        pass
    
    def download(self, url: str) -> None:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        video_id = url.split("?v=")[1]
        try:
            stream.download(filename=f"{video.title}.mp3", output_path="mp3s")
        except OSError:
            stream.download(filename=f"{video_id}.mp3", output_path="mp3s")
        except exceptions.AgeRestrictedError as exception:
            print(exception.error_string)

