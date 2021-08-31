import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

#WAŻNE METODY
"""
current_user_playing_track()
next_track(device_id=None)
"""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="user-modify-playback-state user-read-currently-playing"))
current_song = sp.currently_playing()
#for key, value in current_song['item'].items():
#    print(key, value)
artist_name = current_song['item']['artists'][0]['name']
album_name = current_song['item']['album']['name']
song_name = current_song['item']['name']

print(f"""CURRENTLY PLAYED SONG
Artist: {artist_name}
Album: {album_name}
Song Title: {song_name}""")
