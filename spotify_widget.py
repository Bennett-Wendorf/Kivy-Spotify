from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import ButtonBehavior 
from kivy.uix.label import Label 
from kivy.clock import Clock
import threading
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml

class CircularButton(ButtonBehavior, Label):
    pass

class SpotifyWidget(RelativeLayout):

    spotify = None
    
    def __init__(self, **kwargs):
        # Auth stuff
        self.spotify = self.Spotify_Auth()

        print(self.Get_Playing())

        super(SpotifyWidget, self).__init__(**kwargs)

        Clock.schedule_interval(self.Start_Update_Loop, 10)

    def Get_Playing(self):
        print("Running Get_Playing")
        return self.spotify.current_playback()

    def Start_Update_Loop(self, dt):
        update_thread = threading.Thread(target=self.Get_Playing)
        update_thread.setDaemon(True)
        update_thread.start()

    def Spotify_Auth(self):
        stream = open('./settings.yaml', 'r')
        settings = yaml.load(stream, Loader=yaml.CLoader)

        return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings['client_id'],
                                                          client_secret=settings['client_secret'],
                                                          redirect_uri='http://localhost:8888/redirect',
                                                          scope='user-library-read streaming app-remote-control user-read-playback-state'))