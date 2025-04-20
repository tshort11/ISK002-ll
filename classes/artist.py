class Artist:
    def __init__(self, id, name, genre):
        # Unique identifier for the artist (could be a Spotify ID)
        self.id = id

        # The artist's name (e.g., "Taylor Swift", "Kendrick Lamar")
        self.name = name

        # The genre of music they typically perform (e.g., "Pop", "Hip-Hop")
        self.genre = genre

    def __str__(self):
        # This provides a human-readable string version of the Artist object
        # Useful when printing or displaying the object
        return f"{self.name} (Genre: {self.genre if self.genre else 'Unknown'})"
    
    def to_dict(self):
        # Converts the Artist object into a dictionary format
        # Useful for saving to JSON or transferring data
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre
        }


    
