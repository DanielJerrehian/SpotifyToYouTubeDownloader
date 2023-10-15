import os

from src.downloader import YouTubeMp3Downloader


def test_class_exists():
    assert YouTubeMp3Downloader
    
def test_download(url):
    tube = YouTubeMp3Downloader()
    tube.download(url=url)
    assert os.path.isfile(os.path.join("mp3s", "HUGEL, Cumbiafrica - Morenita (Matroda Remix).mp3"))