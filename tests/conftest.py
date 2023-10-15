import pytest
import os
from dotenv import load_dotenv


def pytest_sessionstart():
    load_dotenv()


@pytest.fixture()
def url():
    url = "https://www.youtube.com/watch?v=B7f1Qp3BKpI"
    yield url
    os.remove(os.path.join("mp3s", "HUGEL, Cumbiafrica - Morenita (Matroda Remix).mp3"))


@pytest.fixture()
def playlist_id():
    playlist_id = "2tUQNiBZ8Xp5jMfM2T7kvx"
    yield playlist_id
    

@pytest.fixture()
def keyword():
    yield "EDC Las Vegas 2023 - Official Trailer"