import yt_dlp
import re
import json
import os
from metadata_manager import add_metadata_to_mp3

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def download_mp3(track, download_path):
    
    filename = sanitize_filename(track.name)
    filepath = f"{download_path}/{filename}"

    query = f"ytsearch:{track.name}"

    yt_dlp_opts = {
        'ffmpeg_location': r'C:\Users\bhavi\ffmpeg\bin\ffmpeg.exe',
        'format': 'bestaudio/best',
        'outtmpl': filepath + ".%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256',
        }],
        'quiet': True,
        'noplaylist': True,
        'ignoreerrors': True,
        'noprogress': True,
        'console_title': False # Disable console title updates
    }

    try:
        with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
            print(f"Downloading: {track.name}")
            ydl.download([query])
            add_metadata_to_mp3(filepath + ".mp3", track)
            return True
    except Exception as e:
        print(f"Error downloading {track.name}: {e}")
        return False


def download_tracks(tracks, download_path):
    if not tracks:
        print("No tracks to download.")
        return

    downloads = 0
    skipped = 0

    downloaded_set = load_downloaded()

    for track in tracks:
        if track.name in downloaded_set:
            print(f"Track '{track.name}' already downloaded. Skipping.")
            skipped += 1
        else:
            if download_mp3(track, download_path):
                append_downloaded(track.name)
                print(f"Downloaded: {track.name}")
                downloads += 1
                downloaded_set.add(track.name)


    print("All downloads completed.")
    print(f"Total downloads: {downloads}, Skipped: {skipped}")

def load_downloaded(filepath="downloaded.txt"):
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()
        
        
def append_downloaded(track_name, filepath="downloaded.txt"):
    with open(filepath, 'a', encoding="utf-8") as f:
        f.write(f"{track_name}\n")
