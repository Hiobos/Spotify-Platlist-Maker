import requests
from scrap import Music
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

music = Music()

class Spot:
    def __init__(self):
        self.playlist, self.date = music.get_music()

        self.client_id = open('keys/client_id.txt', 'r').read()
        self.client_secret = open('keys/client_secret.txt', 'r').read()
        self.redirect_uri = open('keys/redirect_uri.txt', 'r').read()

        #handling authentication
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope='playlist-modify-public'
        ))

    def add_playlist(self):
        # playlist creation, name is the date provided by the user
        user_id = self.sp.current_user()['id']
        playlist = self.sp.user_playlist_create(user=user_id, name=self.date, public=True)
        playlist_id = playlist['id']
        print("✔️ Playlist created:", playlist['external_urls']['spotify'])

        #adding tracks to the playlist, looping through tracks scraped from billboard website
        for track in self.playlist:
            result = self.sp.search(q=track, type='track', limit=1)
            item = result['tracks']['items']
            #checks if any result matches
            if item:
                track_uri = item[0]['uri']
                self.sp.playlist_add_items(playlist_id, [track_uri])
            else:
                print(f"Track not found: {track}")

