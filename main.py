import json
import os
import requests
from rich.console import Console  # For styled and formatted console outputs
from colorama import Fore, Back, Style  # For coloring text in the terminal
from prettytable import PrettyTable  # For creating nice-looking tables in the terminal
from classes.user import User  # User class to manage user-related data
from classes.album import Album  # Album class to manage album data
from classes.song import Song  # Song class to manage song data
from classes.artist import Artist  # Artist class to manage artist data
from classes.spotify_api import SpotifyAPI  # Wrapper class for Spotify API interactions

users = {}  # Global dictionary to store all users

# Function to load saved users from a JSON file
def load_users(filename='users.json'):
    try:
        with open(filename, 'r') as f:
            user_data = json.load(f)  # Load user data from the file
            for data in user_data:
                # Create a new User object for each entry
                user = User(
                    user_id=data['user_id'], 
                    username=data['username'], 
                    email=data['email'], 
                    password=data['password']
                )
                users[user.username] = user  # Store the user object in the global users dictionary
    except FileNotFoundError:
        print("No previous user data found. Starting fresh.")  # If file doesn't exist, create new users
    except json.JSONDecodeError:
        print("Create an account to rate all your favourite music!")  # Handle invalid JSON

# Function to save all users to a JSON file
def save_users(filename='users.json'):
    try:
        with open(filename, 'w') as f:
            json.dump([user.to_dict() for user in users.values()], f)  # Convert user objects to dictionaries and save
        print("Thank you for sharing your favourites! Saved successfully.")
    except IOError as e:
        print(f"Error saving users: {e}")  # Handle file I/O errors

# Helper function to validate user input with custom length constraints
def validate_input(prompt, type_=str, min_length=1, max_length=50):
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length:  # Check length constraints
            try:
                return type_(user_input)  # Attempt to convert the input to the specified type
            except ValueError:
                print(f"Please enter a valid {type_.__name__}.")  # If type conversion fails, show an error
        else:
            print(f"Input must be between {min_length} and {max_length} characters.")  # If length is out of range

# Function to create a new user account
def create_account(username, password):
    user_id = len(users) + 1  # Generate a user ID based on the number of users
    user = User(user_id, username, 'user@example.com', password)  # Create a new User object
    users[username] = user  # Add the user to the global users dictionary
    print(f"Account created for {username}.")
    return user  # Return the new user object

# Check if 'users.json' exists and load existing users, else prompt user to create an account
if os.path.exists('users.json'):
    load_users()
else:
    print("Create an account to rate all your favourite music!")

# Function to log in an existing user
def login(username, password):
    user = users.get(username)  # Retrieve user by username
    if user and user.check_password(password):  # Check if the password is correct
        print(f"Welcome back {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Function for handling the account setup process (create or login)
def account_setup():
    global users
    print("\nWelcome to" + Style.BRIGHT + " interlude!")
    print(Style.RESET_ALL)

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                user_id = len(users) + 1
                user = User(user_id, username, 'user@example.com', password)  # Create the new user object
                create_account(username, password)  # Add the user to the system
                users[username] = user  # Store the user
                print(f"Welcome, {username}. Let's get started!")
                return user  # Return the new user object

            except Exception as e:
                print(f"Error creating account: {e}")

        elif choice == '2':
            try:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if login(username, password):  # Try logging in
                    user = users.get(username)
                    if user:
                        print(f"Login successful! Welcome, {username}.")
                        return user
                    else:
                        print("Error: User not found in the system.")
                else:
                    print("Login failed. Please try again.")
            except Exception as e:
                print(f"Error during login: {e}")

        elif choice == '3':
            print("Goodbye!")
            break  # Exit the account setup loop

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices

# Function to refresh Spotify access token using refresh token
def refresh_access_token(refresh_token):
    import base64
    try:
        url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()  # Authorization header
        }
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token  # Pass the refresh token to get a new access token
        }
        response = requests.post(url, headers=headers, data=payload)  # Send the request
        response.raise_for_status()  # Check if the request was successful
        return response.json().get('access_token')  # Return the new access token
    except requests.exceptions.RequestException as e:
        print(f"Failed to refresh token: {e}")  # Handle request errors
        return None

# Functions to add favorite albums, songs, and artists with ratings to the user's profile
def add_favorite_album_with_rating(user, spotify):
    # ... [Code for adding albums with ratings, and validating inputs, follows a similar pattern]
    pass

def add_favorite_song_with_rating(user, spotify):
    # ... [Code for adding songs with ratings follows a similar pattern]
    pass

def add_favorite_artist(user, spotify):
    # ... [Code for adding artists to favorites follows a similar pattern]
    pass

# Function to discover new music and display it in a formatted table
def discover_music(user, spotify):
    print("\nNew Releases:\n")
    new_music = spotify.get_new_releases()  # Get new releases from Spotify
    new_releases_table = PrettyTable()  # Create a PrettyTable for displaying music info
    new_releases_table.field_names = ["Album Title", "Artist(s)", "Release Date", "Total Tracks", "Listen Here"]

    for album in new_music: 
        album_name = album.get('name', 'Unknown Album')
        release_date = album.get('release_date', 'Unknown Release Date')
        total_tracks = album.get('total_tracks', 'Unknown Track Count')
        artist_name = ', '.join(artist['name'] for artist in album.get('artists', []))  # Combine multiple artists
        album_url = album.get('external_urls', {}).get('spotify', 'No URL available')

        # Add album data to the table
        new_releases_table.add_row([album_name, artist_name, release_date, total_tracks, album_url])

    print(new_releases_table)  # Display the new releases table

# Function to view user profile and display their favorite albums, songs, and artists
def view_user_info(user):
    # Display favorite albums, songs, and artists in pretty tables
    pass

# Main function that drives the program
def main():
    load_users()  # Load existing users from file
    console = Console()  # Create a console object for rich output
    spotify = SpotifyAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', redirect_uri='http://localhost:8888/callback')  # Initialize SpotifyAPI with credentials
    
    while True:
        user = account_setup()  # Setup user account (login or create new)
        if user:
            while True:
                print("\nMenu:")  # Show menu for user options
                choice = input("Choose an option: ")  # Handle different options
                # Call corresponding functions based on user's choice
                if choice == '1':
                    add_favorite_album_with_rating(user, spotify)
                elif choice == '2':
                    add_favorite_song_with_rating(user, spotify)
                elif choice == '3':
                    add_favorite_artist(user, spotify)
                elif choice == '4':
                    discover_music(user, spotify)
                elif choice == '5':
                    view_user_info(user)
                elif choice == '6':
                    save_users()  # Save user data before exiting
                    print("Exiting...")
                    return  # Exit the program
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Run the main program

