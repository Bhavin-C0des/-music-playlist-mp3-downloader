import spotipy
from spotipy.oauth2 import SpotifyOAuth
from track import Track

def get_tracks_from_playlist(playlist_url):
    """
    Fetches tracks from a Spotify playlist given its URL.
    
    Args:
        playlist_url (str): The URL of the Spotify playlist.
        
    Returns:
        list: A list of track objects with details about each track from the playlist.
    """

    tracks = []

    scope = "playlist-read-private playlist-read-collaborative"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlist = sp.playlist(playlist_url)
    print(f"Fetching tracks from playlist: {playlist['name']}")

    results = playlist['tracks']

    while results:

        for song in results['items']:
            track_info = song['track']
            if track_info is None or track_info['name'] is None:
                print("Skipping track with no information.")
                continue

            title = track_info['name']
            artists = [artist['name'] for artist in track_info['artists']]
            album_name = track_info['album']['name']
            release_date = track_info['album']['release_date'] 
            release_year = release_date.split('-')[0] 
            track_number = track_info['track_number']
            images = track_info['album']['images']
            cover_art_url = images[0]['url'] if images else None

            track = Track(title=title, artists=artists, 
                        album_name=album_name, release_year=release_year,
                        track_number=track_number, cover_art_url=cover_art_url)

            tracks.append(track)
            print(f"Added track: {track.name}")

        if results['next']:
                results = sp.next(results)
        else:
                results = None

    print(f"Total tracks fetched: {len(tracks)}")
    return tracks
