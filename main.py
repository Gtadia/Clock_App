from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.button import Button
import datetime
import time
from kivy.clock import Clock

"""
In order to implement darkmode, I think I should use ids on all 
the text/buttons that needs their color/background color changed
"""

class AlarmWindow(Screen):
    from alarm import text_inputted, Set_Alarm

class TimerWindow(Screen):
    from timer import text_inputted, Reset_Timer, Start_Timer

class StopwatchWindow(Screen):
    from stopwatch import Start_Stopwatch

class WorldTimeWindow(Screen):
    def hello(self):
        print("Hello")


class WindowManager(ScreenManager):
    pass

class WindowSwitcher(BoxLayout):
    pass

class MyPopup(Popup):
    # Update code later so that it supports multiple days
    checked_days = []           # Try making this global    (or just don't use the checkbox)
    def days_of_the_week_checkbox(self, checkboxObj, state, day):
        if state:
            self.checked_days.append(day)
        else:
            self.checked_days.remove(day)

        print(self.checked_days)

class ClockApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1)       # Find ways to go between dark and light mode, even if that means just using a canvas
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    ClockApp().run()
