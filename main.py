from kivy.app import App
from kivy.uix.label import Label

class MiApp(App):
    def build(self):
        return Label(text="¡Hola Mundo desde Kivy!")

if __name__ == "__main__":
    MiApp().run()
