import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import json
import time

# I just realized this but we don't need the seconds (but we can copy and past this for the timer)
# Make the 24 hour format a setting and if the setting is on 12, have the am pm button clickable and unclickable when set on 24 hour
def text_inputted(self):
    list_of_labels = [
        self.ids.time_1,
        self.ids.time_2,
        self.ids.time_3,
        self.ids.time_4,
        ]
    list_of_textInputs = [
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


def SetAmPm(self, state):
    changeAmPm = {}
    with open("alarm.json", "r") as open_file: 
        changeAmPm = json.load(open_file)

    changeAmPm["am/pm"] = state
    changeAmPm["is_active"] = True          # Just for debugging purposes

    with open("alarm.json", "w") as open_file:
        open_file.write(json.dumps(changeAmPm, indent=4))


def Set_Alarm(self):
    list_of_time = []
    with open("alarm.json", "r") as open_file:
        for value in json.load(open_file).values():
            list_of_time.append(value)


    list_of_max_num = [59, 59, 24]
    is_valid_format = True
        
    for i in range(2):
        if list_of_time[i] != '':
            if int(list_of_time[i]) > list_of_max_num[i]:
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
    



    list_of_textInputs = [
        self.ids.time_input_minutes, 
        self.ids.time_input_hours  
    ]
    # am/pm: can either store the following values (am, pm, or 24Hour)
    with open("alarm.json", "w") as open_file:
        time_dict = {"minutes": list_of_textInputs[0].text, "hours": list_of_textInputs[1].text, "am/pm": "24Hour", "is_active": True}
        open_file.write(
            json.dumps(time_dict, indent = 4)
            )





    with open("alarm.json", 'r') as open_file:
        my_dict = json.load(open_file)
        if my_dict['is_active']:
            Clock.schedule_interval(run_alarm, 2)
            print("Should be running")


def run_alarm(self):
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print(current_time)

    with open("alarm.json", "r") as open_file:
        alarm_time = json.load(open_file)
        if current_time == f"{alarm_time['hours']}:{alarm_time['minutes']}":
            print("Yep, it works")