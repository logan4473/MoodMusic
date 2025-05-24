from kivy.app import App
from kivy.uix.button import Button

class MoodApp(App):
    def build(self):
        return Button(text='Hello, Mood!')

MoodApp().run()