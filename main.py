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
from kivy.uix.checkbox import CheckBox
import datetime
import time
from kivy.clock import Clock
import json
from kivy.properties import ObjectProperty



"""
In order to implement darkmode, I think I should use ids on all 
the text/buttons that needs their color/background color changed





I THINK MULTIPLE CLOCK.SCHEDULE_INTERVALS() ARE BEING EXECUTED WHEN I PRESS THE START BUTTON MULTIPLE TIMES
"""

"""Code that runs to initialize everything"""
with open("general_settings.json", "r+") as general_settings:
    if len(general_settings.readlines()) < 3:
        setting_dict = {
            "is_dark_mode": False,
            "is_24_format": False,
            "animation_enabled": True
        }
        general_settings.write(json.dumps(setting_dict, indent=4))

from alarm import run_alarm
with open("alarm.json", "r+") as alarm_data:
    if len(alarm_data.readlines()) < 4:
        alarm_dict = {
            "minutes": 0,
            "hours": 0,
            "am/pm": "AM",
            "is_active": False,
            "has_rung": False
        }
        alarm_data.write(json.dumps(alarm_dict, indent=4))


# At the beginning, make sure that every alarm's "has_rung" attribute set to FALSE on launch (The user might have closed the app isntead of clicking the "dismiss alarm" button)
with open("alarm.json", "r") as alarm_data:
    my_dict = json.load(alarm_data)
    # if my_dict['is_active']:
    #     Clock.schedule_interval(run_alarm, 2)
    #     print("Should be running")


with open("timer.json", "r+") as timer_data: 
    if len(timer_data.readlines()) < 3:
        timer_dict = {
            "seconds": 0,
            "minutes": 0,
            "hours": 0
        }
        json_object = json.dumps(timer_dict, indent = 4)
        timer_data.write(json_object)
    

with open("stopwatch.json", "r+") as stopwatch_data:
    if len(stopwatch_data.readlines()) < 4:
        stopwatch_dict = {
            "miliseconds": 0,
            "seconds": 0,
            "minutes": 0,
            "hours": 0
        }
        json_object = json.dumps(stopwatch_dict, indent = 4)
        stopwatch_data.write(json_object)


class AlarmWindow(Screen):
    from alarm import text_inputted, Set_Alarm, SetAmPm

class TimerWindow(Screen):
    from timer import text_inputted, Reset_Timer, Start_Timer

class StopwatchWindow(Screen):
    from stopwatch import get_time, Start_Stopwatch

class WorldTimeWindow(Screen):
    def hello(self):
        print("Hello")

class GeneralSettingsWindow(Screen):
    from GeneralSettings import dark_light_mode_change, hour_format_change, enable_animation, reset_data

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

    def repeat_or_ring_once(self, is_active):
        print(is_active)
        if is_active: 
            print(is_active)
            for child in reversed(self.ids.checkbox_days.children):         # In a certain layout, it will traverse through the entire list to find all the children/widgets
                if isinstance(child, CheckBox):   
                    child.disabled = True
        else:
            print(is_active)
            for child in reversed(self.ids.checkbox_days.children):         # In a certain layout, it will traverse through the entire list to find all the children/widgets
                if isinstance(child, CheckBox):   
                    child.disabled = False

class ClockApp(App):
    with open("general_settings.json", 'r') as open_file:
        settings = json.load(open_file)
        dark_mode = ObjectProperty(settings['is_dark_mode'])
        hour_format = ObjectProperty(settings['is_24_format'])
        animation = ObjectProperty(settings['animation_enabled'])
        
    def build(self):
        Window.clearcolor = (1, 1, 1)       # Find ways to go between dark and light mode, even if that means just using a canvas
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    ClockApp().run()