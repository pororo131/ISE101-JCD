from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutDemo(App):
    def build(self):
        layout = AnchorLayout(anchor_x="left", anchor_y="top")  # top-left corner
        layout.add_widget(Button(text="I’m in the top-left!"))
        return layout

if __name__ == "__main__":
    AnchorLayoutDemo().run()
