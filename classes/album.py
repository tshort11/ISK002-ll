class Album:
    def __init__(self, id, title, artist, release_date, genre=None):
        # Unique identifier for the album
        self.id = id

        # Title of the album
        self.title = title

        # Name of the artist or band who made the album
        self.artist = artist

        # Release date of the album
        self.release_date = release_date

        # Optional genre of the album (default is None if not provided)
        self.genre = genre 

        # Rating will be assigned later by the user (default is None)
        self.rating = None

    # Converts the album object into a dictionary format, useful for saving to JSON
    def to_dict(self):
        return {
            'title': self.title,
            'artist': self.artist,
            'release_date': self.release_date
            # 'rating': self.rating
        }





 

        



