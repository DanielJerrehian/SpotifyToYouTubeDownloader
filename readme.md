# SpotifyToYouTubeDownloader
Download all the songs in your Spotify playlist as MP3s

## How To:
- Set the following environment variables in a ```.env``` file (Spotify and YouTube developer accounts required):
    - ```SpotifyClientId```
    - ```SpotifyClientSecret```
    - ```YouTubeApiKey```
- Replace the ```playlist_id``` argument in the function call in ```main.py``` with your playlist
- Execute ```python -m main```
- Songs will be downloaded to the directory ```mp3s``` 
- Enjoy!

## Tests
- Tests are located in the directory ```tests/```
- Run the tests by executing ```python -m pytest```

## Known Issues:
- The YouTube Data API V3 quota is low and only allows 100 video searches by keyword per day, meaning the tool will only work for the first 100 songs in a playlist
- Videos with age restricted content are not downloaded and a message will be printed to the console with the corresponding video ID
- I wrote this program very quickly, the orchestration in ```main.py``` needs to be updated on a rainy day

## Thoughts:
- Maybe I'll turn this into a package someday?