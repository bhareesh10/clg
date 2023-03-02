import math

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

        self.t1 = Label(text='time1:(sec)')
        self.layout.add_widget(self.t1)

        self.ti1 = TextInput()
        self.layout.add_widget(self.ti1)

        self.t2 = Label(text='time2(sec):')
        self.layout.add_widget(self.t2)

        self.ti2 = TextInput()
        self.layout.add_widget(self.ti2)

        self.t3 = Label(text='time3:(sec)')
        self.layout.add_widget(self.t3)

        self.ti3 = TextInput()
        self.layout.add_widget(self.ti3)

        self.h = Label(text='h:')
        self.layout.add_widget(self.h)

        self.hi = TextInput()
        self.layout.add_widget(self.hi)

        self.calculate_button = Button(text='Calculate resistance', on_press=self.calculate_resistance)
        self.layout.add_widget(self.calculate_button)

        self.add_widget(self.layout)

    def calculate_resistance(self, *args):
        t1 = float(self.ti1.text)
        t2 = float(self.ti2.text)
        t3 = float(self.ti3.text)
        h = float(self.hi.text)

        t = (t1 + t2 + t3) / 3
        k = math.sqrt((math.pow(t * 2 * 3.14, 2)/9.81 * h) - math.pow(h, 2) )
        result_screen = ResultScreen(resistance=k)
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