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
    print(changeAmPm)

    with open("alarm.json", "w") as open_file:
        open_file.write(json.dumps(changeAmPm, indent=4))




"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    SET ALARM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# Make the START ALARM (currently "Does this work?") grayed out until all the information is filled out.

def Set_Alarm(self):
    list_of_textInputs = [
        self.ids.time_input_minutes, 
        self.ids.time_input_hours  
    ]

    alarm_data = []
    with open("alarm.json", "r") as open_file:
        for value in json.load(open_file).values():
            alarm_data.append(value)


    max_hour = int()
    if alarm_data[2] == "24":
        max_hour = 23
    else: 
        max_hour = 13


    list_of_max_num = [59, max_hour]
    print(f"Max Hour: {max_hour}")
    is_valid_format = True
        
    for i in range(2):
        if alarm_data[i] != '':
            if int(alarm_data[i]) > list_of_max_num[i]:
                is_valid_format = False
                list_of_textInputs[i].text = "0"     # If the format is invalid, it's only that thing (minute or hour) is going to return back to 0
                break

    """POPUP"""
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
    """POPUP ENDS"""
    

    # am/pm: can either store the following values (am, pm, or 24Hour)
    with open("alarm.json", "w") as open_file:
        time_dict = {"minutes": list_of_textInputs[0].text, "hours": list_of_textInputs[1].text, "am/pm": alarm_data[2], "is_active": True, "has_rung": False}
        open_file.write(
            json.dumps(time_dict, indent = 4)
            )




    with open("alarm.json", 'r') as open_file:
        my_dict = json.load(open_file)
        if my_dict['is_active']:
            self.event = Clock.schedule_interval(run_alarm, 2)
            print("Should be running")
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    SET ALARM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""





def run_alarm(self):
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print(f"acutal current time: {current_time}")


    alarm_time = {}
    with open("alarm.json", "r") as open_file:
        alarm_time = json.load(open_file)   

        hours = int(alarm_time['hours'])
        print(alarm_time)


        if alarm_time['am/pm'] != '24':
            if alarm_time['am/pm'] == 'PM' and alarm_time['hours'] != '12':
                hours = int(alarm_time['hours']) + 12
            elif alarm_time['am/pm'] == 'AM' and alarm_time['hours'] == '12':
                hours = "0"

        if current_time == f"{hours}:{alarm_time['minutes']}":
            print("Yep, it works")
            ring_alarm()



        print(f"hours: {hours}")



            


def ring_alarm(self):
    self.event.cancel()
    print("It has been done")

    alarm_dict = {}
    with open('alarm.json', 'r') as open_file:
        alarm_dict = json.load(open_file)


    # Have an option where the alarm can either be rung once and is_active is set to False until it is turned back on or 
    # if it's a weekly thing, check whether or not today is a day that the alarm should ring.
    alarm_dict["has_rung"] = True


    with open("alarm.json", 'w') as open_file:
        open_file.write(json.dumps(json.dumps(alarm_dict, indent=4)))
