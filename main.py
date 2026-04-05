from kivy.app import App
from kivy.uix.label import Label


class YSocietyApp(App):
    def build(self):
        return Label(
            text="Hello World from Y-SOCIETY-APP",
            font_size="24sp",
            halign="center",
            valign="middle"
        )


if __name__ == "__main__":
    YSocietyApp().run()
