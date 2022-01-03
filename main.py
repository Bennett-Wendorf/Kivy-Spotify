from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App

from kivy.clock import Clock
import threading

# Set the default size of the window to 240x160, 1/4 the size of my 3.5" touchscreen module for a Raspberry Pi
Config.set('graphics', 'width', '240')
Config.set('graphics', 'height', '160')
Window.size=(240,160)

class SpotifyWidget(RelativeLayout):
    
    def __init__(self, **kwargs):
        # Auth stuff

        self.Get_Playing()

        super(SpotifyWidget, self).__init__(**kwargs)

        Clock.schedule_interval(self.Start_Update_Loop, 10)

    def Get_Playing(self):
        print("Running Get_Playing")

    def Start_Update_Loop(self, dt):
        update_thread = threading.Thread(target=self.Get_Playing)
        update_thread.setDaemon(True)
        update_thread.start()

class KivySpotifyApp(App):
    def build(self):
        super(KivySpotifyApp, self).build()
        return SpotifyWidget()

if __name__ == '__main__':
    KivySpotifyApp().run()
