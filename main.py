from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from spotify_widget import SpotifyWidget

# Set the default size of the window to 240x160, 1/4 the size of my 3.5" touchscreen module for a Raspberry Pi
Config.set('graphics', 'width', '240')
Config.set('graphics', 'height', '160')
Window.size=(240,160)

class KivySpotifyApp(App):
    def build(self):
        super(KivySpotifyApp, self).build()
        return SpotifyWidget()

if __name__ == '__main__':
    KivySpotifyApp().run()
