class Song:
    def __init__(self, id, title, artist, album, duration_ms, release_date=None):
        # Unique identifier for the song (e.g., from Spotify)
        self.id = id

        # Title of the song (e.g., "Blinding Lights")
        self.title = title

        # Name of the artist or band who performed the song
        self.artist = artist

        # Album the song belongs to
        self.album = album

        # Duration of the song in milliseconds (could change)
        self.duration_ms = duration_ms

        # Optional release date of the song
        self.release_date = release_date  

    def __repr__(self):
        # Developer-friendly representation of the Song object
        # Useful for debugging or logging
        return (f"Song(id={self.id}, title={self.title}, "
                f"artist={self.artist}, album={self.album}, duration={self.duration_ms} ms)")

    def to_dict(self):
        # Converts the Song object into a dictionary
        # Makes it easier to serialise (e.g., into JSON)
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'album': self.album,
            'duration_ms': self.duration_ms,
            'release_date': self.release_date
        }
