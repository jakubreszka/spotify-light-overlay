import os
import spotipy
import sys
import requests
from PySide6 import QtCore, QtWidgets, QtGui
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
album_cover = current_song['item']['album']['images'][2]['url']

print(f"""CURRENTLY PLAYED SONG
Artist: {artist_name}
Album: {album_name}
Song Title: {song_name}
Album Cover: {album_cover}""")

class SpotifyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.artist_text = QtWidgets.QLabel(f"Artist: {artist_name}",
                                     alignment=QtCore.Qt.AlignCenter)
        self.song_text = QtWidgets.QLabel(f"Song: {song_name}",
                                     alignment=QtCore.Qt.AlignCenter)
        self.album_text = QtWidgets.QLabel(f"Song: {album_name}",
                                     alignment=QtCore.Qt.AlignCenter)
        pic = QtGui.QImage().loadFromData(requests.get(album_cover).content)
        self.lbl = QtWidgets.QLabel(pic)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.artist_text)
        self.layout.addWidget(self.song_text)
        self.layout.addWidget(self.album_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = SpotifyApp()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
