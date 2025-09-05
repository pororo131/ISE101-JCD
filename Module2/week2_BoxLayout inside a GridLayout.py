from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class NestedLayoutDemo(App):
    def build(self):
        # Outer GridLayout with 2 columns
        grid = GridLayout(cols=2)

        # Inner BoxLayout (vertical) to put inside the GridLayout
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text="Box Btn 1"))
        box.add_widget(Button(text="Box Btn 2"))

        # Add BoxLayout as first cell of GridLayout
        grid.add_widget(box)

        # Add other buttons directly into GridLayout
        grid.add_widget(Button(text="Grid Btn 1"))
        grid.add_widget(Button(text="Grid Btn 2"))
        grid.add_widget(Button(text="Grid Btn 3"))

        return grid

if __name__ == "__main__":
    NestedLayoutDemo().run()
