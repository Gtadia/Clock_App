from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import re
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.button import Button

"""
In order to implement darkmode, I think I should use ids on all 
the text/buttons that needs their color/background color changed
"""

class AlarmWindow(Screen):
    # I just realized this but we don't need the seconds (but we can copy and past this for the timer)
    def text_inputted(self):
        textInput = self.ids.alarm_time_input.text
        list_of_labels = [
            self.ids.time_1,
            self.ids.time_2,
            self.ids.time_3,
            self.ids.time_4,
            self.ids.time_5,
            self.ids.time_6
            ]
        

        print(self.ids.alarm_time_input.text)      

        if len(textInput) > 6:
            # Prevents going past the hours section 
            textInput = textInput[0:6]
        if "." in textInput:
            # Removes the periods (because we don't need them)
            textInput = re.sub(".", "", textInput)

        self.ids.alarm_time_input.text = textInput

        for i in range(6):
            try:
                list_of_labels[i].text = textInput[i]
            except: 
                list_of_labels[i].text = "0"


class TimerWindow(Screen):
    list_of_labels = []
    list_of_textInputs = []

    def text_inputted(self):
        list_of_labels = [
            self.ids.time_1,
            self.ids.time_2,
            self.ids.time_3,
            self.ids.time_4,
            self.ids.time_5,    
            self.ids.time_6
            ]
        list_of_textInputs = [
            self.ids.time_input_seconds, 
            self.ids.time_input_minutes, 
            self.ids.time_input_hours  
        ]
    
        index_num = 0
        for i in range(len(list_of_textInputs)):
            if len(list_of_textInputs[i].text) > 2:
                list_of_textInputs[i].text = list_of_textInputs[i].text[0:2]
            if "." in list_of_textInputs[i].text:
                list_of_textInputs[i].text = re.sub(".", "", list_of_textInputs[i].text)
        
            for j in range(2):
                try:
                    if len(list_of_textInputs[i].text) == 2:
                        if j == 1:  
                            # Switches the last digit's location with the first digit's location
                            list_of_labels[index_num].text = list_of_textInputs[i].text[0]
                            list_of_labels[index_num - 1].text = list_of_textInputs[i].text[1]
                    else:
                        list_of_labels[index_num].text = list_of_textInputs[i].text[j]
                except: 
                    list_of_labels[index_num].text = "0"
                index_num += 1
    

    def Start_Timer(self):
        list_of_textInputs = [
            self.ids.time_input_seconds, 
            self.ids.time_input_minutes, 
            self.ids.time_input_hours  
        ]
        list_of_max_num = [59, 59, 23]
        is_valid_format = True
        
        # Move this statement to run after the "start button runs"  
        for i in range(3):
            if list_of_textInputs[i].text != '':
                if int(list_of_textInputs[i].text) > list_of_max_num[i]:
                    is_valid_format = False
                    break

        if not is_valid_format:
            close_button = Button(text="Dismiss")
            boxlayout_w = BoxLayout(orientation = 'vertical')
            boxlayout_w.add_widget(Label(text='This is not a valid answer')) 
            boxlayout_w.add_widget(close_button)
            
            popup = Popup(title='ERROR', auto_dismiss=False, 
            size_hint=(0.8, 0.3), pos_hint={"x": 0.1, "top": 0.9}, 
            content=boxlayout_w)
            close_button.bind(on_release = popup.dismiss)

            popup.open()


class StopwatchWindow(Screen):
    pass

class WorldTimeWindow(Screen):
    pass

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