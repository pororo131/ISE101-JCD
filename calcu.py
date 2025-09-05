from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        # Display
        self.display = TextInput(multiline=False, readonly=True, halign="right", font_size=32)
        layout.add_widget(self.display)

        # Buttons grid
        buttons_layout = GridLayout(cols=4, spacing=5)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for text in buttons:
            btn = Button(text=text, font_size=24)
            btn.bind(on_press=self.on_button_press)  # bind function
            buttons_layout.add_widget(btn)

        layout.add_widget(buttons_layout)
        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""  # Clear display
        elif text == "=":
            pass  # Do nothing for now (no compute function yet)
        else:
            self.display.text += text  # Add button text to display


if __name__ == "__main__":
    CalculatorApp().run()

