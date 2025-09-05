from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutDemo(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')  # Changed to vertical
        layout.add_widget(Button(text="Button 1"))
        layout.add_widget(Button(text="Button 2"))
        layout.add_widget(Button(text="Button 3"))
        return layout

if __name__ == "__main__":
    BoxLayoutDemo().run()
