from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
class CalculatorApp(App):
    def build(self):
        main_layout =BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.input_box = TextInput(
            font_size=48,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0, 0, 0),
            padding=(25, 25),
            font_name="Roboto"   
        )
        
        main_layout.add_widget(self.input_box)
        buttons_layout = GridLayout(rows=4, cols=4, spacing=5, padding=5)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        for text in buttons:
            btn = Button(
                text=text,
                font_size=32,
                background_color=(0.25, 0.25, 0.25, 1),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_button_press(self, instance):
        text = instance.text
        if text =="C":
            self.input_box.text = ""
        elif text == "=":
            try:
                self.input_box.text = str(eval(self.input_box.text))
                
            except Exception:
                
                self.input_box.text = "Error"
        else:
            
          self.input_box.text += text
                
    
if __name__ == "__main__":
    CalculatorApp().run()
    
        