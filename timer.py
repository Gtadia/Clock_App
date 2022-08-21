import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import json

def text_inputted(self):
    self.list_of_labels = [
        self.ids.time_1.text,
        self.ids.time_2.text,
        self.ids.time_3.text,
        self.ids.time_4.text,
        self.ids.time_5.text,    
        self.ids.time_6.text
        ]
    self.list_of_textInputs = [
        self.ids.time_input_seconds.text, 
        self.ids.time_input_minutes.text, 
        self.ids.time_input_hours.text  
    ]

    index_num = 0
    for i in range(len(self.list_of_textInputs)):
        if len(self.list_of_textInputs[i]) > 2:
            self.list_of_textInputs[i] = self.list_of_textInputs[i][0:2]
        if "." in self.list_of_textInputs[i]:
            self.list_of_textInputs[i] = re.sub(".", "", self.list_of_textInputs[i])
        
        
        for j in range(2):
            try:
                if len(self.list_of_textInputs[i]) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num] = self.list_of_textInputs[i][0]
                        self.list_of_labels[index_num - 1] = self.list_of_textInputs[i][1]
                else:
                    self.list_of_labels[index_num] = self.list_of_textInputs[i][j]
            except: 
                self.list_of_labels[index_num] = "0"
            index_num += 1
    
def Start_Timer(self, state):
    timer_dict = dict()
    timer_keys = ["seconds", "minutes", "hours"]
    for i in range(len(timer_keys)):
        try:
            timer_dict[timer_keys[i]] = int(self.list_of_textInputs[0])
        except:
            timer_dict[timer_keys[i]] = 0
    with open("timer.json", "w") as open_file:
        open_file.write(json.dumps(timer_dict))


    if state == "START":
        self.event = Clock.schedule_interval(lambda dt: get_time(self, dt), 1)
        self.ids.startStopButton.text = "STOP"
    else:
        self.event.cancel()
        self.ids.startStopButton.text = "START"

def Reset_Timer(self):
    self.ids.time_input_seconds.text = '' 
    self.ids.time_input_minutes.text = ''
    self.ids.time_input_hours.text = ''


def get_time(self, deltaTime):
    with open("timer.json", "r") as open_file:
        self.timer = json.load(open_file)

    print(self.timer)

    increment = 1
    self.list_of_textInputs[0] = str(self.list_of_textInputs[0] - increment * deltaTime)
    if float(self.list_of_textInputs[0]) <= 0:
        self.list_of_textInputs[1] = str(self.list_of_textInputs[1] - 1)
        self.list_of_textInputs[0] = "0"
    if int(self.list_of_textInputs[1]) <= 0:
        self.list_of_textInputs[2] = str(self.list_of_textInputs[2] - 1)
        self.list_of_textInputs[1] = "0"
    if int(self.list_of_textInputs[2]) <= 0: 
        increment = 0

    with open("timer.json", "w"):
        open_file.write(
            json.dumps(
            {"seconds": int(self.list_of_textInputs[0]), 
            "minutes": int(self.list_of_textInputs[1]),
            "hours": int(self.list_of_textInputs[2])
            })
        )




    print(f"{self.hours} : {self.minutes} : {self.seconds}")
    print(deltaTime)

    index_num = 0
    for i in range(len(self.list_of_textInputs)):        
# Add hours label widget when we get there (try not to have it there when we don't need it)

        for j in range(2):
            try:
                if len(self.list_of_textInputs[i]) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num] = self.list_of_textInputs[i][0]
                        self.list_of_labels[index_num - 1] = self.list_of_textInputs[i][1]
                else:
                    self.list_of_labels[index_num] = self.list_of_textInputs[i][j]
            except: 
                self.list_of_labels[index_num] = "0"
            index_num += 1