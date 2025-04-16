import requests

from scrap import Music
music = Music()

#profil_id: 31i4urplmukhyu5u6ljp4dadsu5q

class Spot:
    def __init__(self):
        self.playlist, self.date = music.get_music()

        self.client_id = open('keys/client_id.txt', 'r').read()
        self.client_secret = open('keys/client_secret.txt', 'r').read()
        self.redirect_uri = open('keys/redirect_uri.txt', 'r').read()

    def authorize(self):
        endpoint = 'https://accounts.spotify.com/authorize?'
        parameters = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': 'playlist-modify-public'
        }

        response = requests.get(url=endpoint, params=parameters)
        print(response)
        print(response.text)

    def get_profile(self):
        endpoint = 'https://api.spotify.com/v1/me'




