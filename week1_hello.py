from kivy.app import App
from kivy.uix.label import Label

class HelloWorld(App):
    def build(self):
        return Label(
            text="BSIS - DAVID CLARENCE!",   # Exercise 2
            font_size="40sp"             # Exercise 3 (Challenge)
        )

if __name__ == "__main__":
    HelloWorld().run()
