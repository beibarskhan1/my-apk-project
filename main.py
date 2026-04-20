from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Привет из Казахстана! Это мое первое APK')

if __name__ == '__main__':
    MyApp().run()