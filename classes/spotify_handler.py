import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyHandler:
    def __init__(self, client_id, client_secret):
  
        # Initialises the SpotifyHandler with client credentials and sets up the Spotipy client.
        
        # Parameters:
       #  - client_id: Your Spotify API client ID.
        # - client_secret: Your Spotify API client secret.
     
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = self.authenticate()  # Authenticate when the object is created

    def authenticate(self):
        
       # Authenticates using Spotify's Client Credentials Flow.
       # This flow is used for non-user specific requests (e.g., searching, browsing).
      
        auth_manager = SpotifyClientCredentials(
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        return spotipy.Spotify(auth_manager=auth_manager)

    def search_album(self, album_name):
        
       # Searches for albums on Spotify by name.

       # Parameters:
       # - album_name: A string representing the name of the album to search for.

        #  Returns:
        # - The full result dictionary returned by the Spotify Web API, which contains:
        #  - A list of matching album objects
        # - Metadata like pagination info, album IDs, artists, images, etc.
        
        results = self.sp.search(q=album_name, type='album')
        return results

