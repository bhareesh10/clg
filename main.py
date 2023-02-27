from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.voltage_label = Label(text='Enter voltage:')
        self.layout.add_widget(self.voltage_label)

        self.voltage_input = TextInput()
        self.layout.add_widget(self.voltage_input)

        self.current_label = Label(text='Enter current:')
        self.layout.add_widget(self.current_label)

        self.current_input = TextInput()
        self.layout.add_widget(self.current_input)

        self.calculate_button = Button(text='Calculate resistance', on_press=self.calculate_resistance)
        self.layout.add_widget(self.calculate_button)

        self.add_widget(self.layout)

    def calculate_resistance(self, *args):
        voltage = float(self.voltage_input.text)
        current = float(self.current_input.text)
        resistance = voltage / current
        result_screen = ResultScreen(resistance=resistance)
        self.manager.switch_to(result_screen)


class ResultScreen(Screen):
    def __init__(self, resistance, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.result_label = Label(text=f'Resistance: {resistance:.2f} ohms')
        self.layout.add_widget(self.result_label)

        self.back_button = Button(text='Back', on_press=self.go_to_input_screen)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def go_to_input_screen(self, *args):
        self.manager.switch_to(InputScreen())


class ResistanceCalculatorApp(App):
    def build(self):
        screen_manager = ScreenManager()
        input_screen = InputScreen(name='input')
        screen_manager.add_widget(input_screen)
        return screen_manager


if __name__ == '__main__':
    ResistanceCalculatorApp().run()
