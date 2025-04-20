import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import base64
import time  # Needed for checking token expiry
from spotipy.exceptions import SpotifyException  # Handle API errors

class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri):
        # Spotify API credentials
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        # Scope for permissions; this one allows reading the user's top tracks
        self.scope = "user-top-read"

        # Authenticate the user and store the Spotipy client
        self.sp = self.authenticate()

        # Tokens and expiration time
        self.access_token = None
        self.refresh_token = None
        self.token_expires = None 

    def refresh_access_token(self):
        
        # If the refresh token exists, send a request to Spotify's token endpoint to get a new access token when it expires.
        
        if self.refresh_token:
            url = 'https://accounts.spotify.com/api/token'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            payload = {
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
                'client_id': self.client_id,
                'client_secret': self.client_secret,
            }
            response = requests.post(url, headers=headers, data=payload)

            if response.status_code == 200:
                data = response.json()
                self.access_token = data['access_token']
                self.token_expires = time.time() + data['expires_in']
                print("Access token refreshed successfully.")
            else:
                print("Failed to refresh access token:", response.json())
        else:
            print("No refresh token available.")

    def refresh_token_if_expired(self):
    
        # Checks if the current access token has expired and refreshes it if needed.
       
        if self.token_expires and (time.time() > self.token_expires):
            self.refresh_access_token()

    def authenticate(self):
        
        # Authenticates the user using SpotifyOAuth and returns a Spotipy client object.
        
        sp_oauth = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope
        )
        token_info = sp_oauth.get_access_token(as_dict=False)
        return spotipy.Spotify(auth=token_info)

    def search_album(self, album_name):
        
        # Searches Spotify for an album by name.
        # Returns the first match with basic details.
    
        result = self.sp.search(q='album:' + album_name, type='album')
        albums = result['albums']['items']
        if albums:
            album = albums[0]
            return {
                'title': album['name'],
                'artist': album['artists'][0]['name'],
                'release_date': album['release_date'],
                'total_tracks': album['total_tracks']
            }
        return None

    def search_song(self, song_name):
        
        #Searches Spotify for a song by name.
        # Returns details for the top result.
       
        result = self.sp.search(q='track:' + song_name, type='track')
        tracks = result['tracks']['items']
        if tracks:
            track = tracks[0]
            return {
                'title': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'duration_ms': track['duration_ms']
            }
        return None

    def search_artist(self, artist_name):
        
        # Searches Spotify for an artist by name.
        # returns the first match or None if not found.
        
        self.refresh_token_if_expired()
        try:
            result = self.sp.search(q='artist:' + artist_name, type='artist')
            artists = result['artists']['items']
            if artists:
                artist = artists[0]
                return {
                    'id': artist['id'],
                    'name': artist['name'],
                    'genre': artist['genres'][0] if artist['genres'] else 'Unknown'
                }
            return None
        except SpotifyException as e:
            print("Error searching for artist:", e)
            return None

    def get_new_releases(self):
       #  Gets the 10 most recent new album releases globally.
        results = self.sp.new_releases(limit=10)
        return results['albums']['items']

    def get_top_tracks(self):
      # Retrieves the current user’s top tracks.
        results = self.sp.current_user_top_tracks(limit=10)
        return results['items']
