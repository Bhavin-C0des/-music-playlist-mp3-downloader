class Track():
    def __init__(self, title: str, artists: list, album_name: str = None, release_year: str = None, track_number: int = None, cover_art_url: str = None):
        self.title = title
        self.artists = artists if artists else ["Unknown Artist"]
        self.primary_artist = artists[0] if artists else "Unknown Artist"
        self.contributors = artists[1:] if len(artists) > 1 else []
        self.album_name = album_name
        self.release_year = release_year
        self.track_number = track_number
        self.cover_art_url = cover_art_url
        self.album_artist = self.artists[0]
        if not self.album_artist:
            self.album_artist = "Unknown Artist"

        self.formatted_artists = ', '.join(artists)
        self.name = f"{title} - {self.formatted_artists}"

        self.id3_artists = ', '.join(artists) # for metadata

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name