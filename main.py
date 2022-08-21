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
import json

"""
In order to implement darkmode, I think I should use ids on all 
the text/buttons that needs their color/background color changed
"""

"""Code that runs to initialize everything"""
from alarm import run_alarm
with open("alarm.json", "r+") as alarm_data:
    if len(alarm_data.readlines()) < 4:
        alarm_dict = {
            "minutes": 0,
            "hours": 0,
            "am/pm": "AM",
            "is_active": False
        }
        alarm_data.write(json.dumps(alarm_dict, indent=4))

with open("alarm.json", "r") as alarm_data:
    my_dict = json.load(alarm_data)
    if my_dict['is_active']:
        Clock.schedule_interval(run_alarm, 2)
        print("Should be running")


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
    # def Start_Timer(self):
    #     print("Hi")
    #     self.list_of_textInputs = [
    #         self.ids.time_input_seconds, 
    #         self.ids.time_input_minutes, 
    #         self.ids.time_input_hours  
    #     ]

    #     self.seconds = self.list_of_textInputs[0].text
    #     self.minutes = self.list_of_textInputs[1].text
    #     self.hours = self.list_of_textInputs[2].text


    #     list_of_max_num = [59, 59, 23]
    #     is_valid_format = True
            
    #     for i in range(3):
    #         if self.list_of_textInputs[i].text != '':
    #             if int(self.list_of_textInputs[i].text) > list_of_max_num[i]:
    #                 is_valid_format = False
    #                 break

    #     if not is_valid_format:
    #         close_button = Button(text="Dismiss")
    #         boxlayout_w = BoxLayout(orientation = 'vertical')
    #         boxlayout_w.add_widget(Label(text='This is not a valid answer')) 
    #         boxlayout_w.add_widget(close_button)
            
    #         popup = Popup(title='ERROR', auto_dismiss=False, 
    #         size_hint=(0.8, 0.3), pos_hint={"x": 0.1, "top": 0.9}, 
    #         content=boxlayout_w)
    #         close_button.bind(on_release = popup.dismiss)

    #         popup.open()



    #     if self.ids.Timer_StartStopButton == "START":
    #         Clock.schedule_interval(self.get_time, 1)
    #         self.ids.Timer_StartStopButton.text = "STOP"
        
    #     if self.is_time_up:
    #         Clock.unschedule(self.get_time)
    #         self.ids.Timer_StartStopButton.text = "START"

class StopwatchWindow(Screen):
    from stopwatch import get_time, Start_Stopwatch
    

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