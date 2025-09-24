import eyed3
import requests
from track import Track

def add_metadata_to_mp3(file_path: str, track: Track):
    audiofile = eyed3.load(file_path)
    if audiofile.tag is None:
        audiofile.initTag()
    
    audiofile.tag.title = track.title
    audiofile.tag.artist = track.primary_artist
    audiofile.tag.album = track.album_name
    audiofile.tag.album_artist = track.album_artist
    audiofile.tag.release_date = track.release_year
    audiofile.tag.original_release_date = track.release_year
    audiofile.tag.track_num = (track.track_number or 0, 0)

    if track.cover_art_url:
        response = requests.get(track.cover_art_url)
        if response.status_code == 200:
            audiofile.tag.images.set(3, response.content, 'image/jpeg', u'Cover Art')
        else:
            print(f"Failed to fetch cover art for {track.name}: {response.status_code}")

    audiofile.tag.save()
    print(f"Metadata added to {file_path}")