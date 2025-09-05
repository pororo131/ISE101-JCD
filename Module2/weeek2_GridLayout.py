from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutDemo(App):
    def build(self):
        layout = GridLayout(cols=3)  # 3 columns → makes 3x3 when 9 buttons
        for i in range(1, 10):       # Loop to create 9 buttons
            layout.add_widget(Button(text=f"Button {i}"))
        return layout

if __name__ == "__main__":
    GridLayoutDemo().run()
