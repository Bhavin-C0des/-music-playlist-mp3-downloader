import os
from dotenv import load_dotenv
from spotipy_utils import get_tracks_from_playlist
from downloader import download_tracks
from track import Track

def main():
    load_dotenv()

    # Download path setup
    download_path = os.getenv("DOWNLOAD_PATH", "downloads")
    if not os.path.exists(download_path) and download_path != "downloads":
        print("Download path does not exist. Falling back to default 'downloads' directory.")
        download_path = "downloads"
        if not os.path.exists(download_path):
            os.makedirs(download_path)
            print(f"Created default download directory: {download_path}")
    print(f"Download path is set to: {download_path}")

    playlist_url = input("Enter your Spotify playlist URL: ").strip()

    tracks = get_tracks_from_playlist(playlist_url)
    download_tracks(tracks, download_path)

if __name__ == "__main__":
    main()