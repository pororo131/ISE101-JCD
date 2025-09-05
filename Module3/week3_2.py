from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class NameApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=10, spacing=10)

        self.label = Label(text="Enter your name:")
        layout.add_widget(self.label)

        self.text_input = TextInput(multiline=False)
        layout.add_widget(self.text_input)

        # Submit button
        submit_btn = Button(text="Submit")
        submit_btn.bind(on_press=self.on_submit)
        layout.add_widget(submit_btn)

        # Clear button
        clear_btn = Button(text="Clear")
        clear_btn.bind(on_press=self.on_clear)
        layout.add_widget(clear_btn)

        return layout

    def on_submit(self, instance):
        name = self.text_input.text.strip()
        if name:  # if not empty
            self.label.text = f"Hello, {name}!"
        else:  # empty input
            self.label.text = "Please enter a name."

    def on_clear(self, instance):
        self.text_input.text = ""  # clear the text field
        self.label.text = "Enter your name:"  # reset label

if __name__ == "__main__":
    NameApp().run()
