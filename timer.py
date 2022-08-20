import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

def text_inputted(self):
    self.list_of_labels = [
        self.ids.time_1,
        self.ids.time_2,
        self.ids.time_3,
        self.ids.time_4,
        self.ids.time_5,    
        self.ids.time_6
        ]
    self.list_of_textInputs = [
        self.ids.time_input_seconds, 
        self.ids.time_input_minutes, 
        self.ids.time_input_hours  
    ]

    index_num = 0
    for i in range(len(self.list_of_textInputs)):
        if len(self.list_of_textInputs[i].text) > 2:
            self.list_of_textInputs[i].text = self.list_of_textInputs[i].text[0:2]
        if "." in self.list_of_textInputs[i].text:
            self.list_of_textInputs[i].text = re.sub(".", "", self.list_of_textInputs[i].text)
        
        
        for j in range(2):
            try:
                if len(self.list_of_textInputs[i].text) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num].text = self.list_of_textInputs[i].text[0]
                        self.list_of_labels[index_num - 1].text = self.list_of_textInputs[i].text[1]
                else:
                    self.list_of_labels[index_num].text = self.list_of_textInputs[i].text[j]
            except: 
                self.list_of_labels[index_num].text = "0"
            index_num += 1
    

def Reset_Timer(self):
    self.ids.time_input_seconds.text = '' 
    self.ids.time_input_minutes.text = ''
    self.ids.time_input_hours.text = ''







def get_time(self, deltaTime):
    self.seconds -= (deltaTime)
    if self.seconds < 0:
        self.minutes -= 1
        self.seconds = 59
    if self.minutes < 0:
        self.hours -= 1
        self.minutes =59
    if self.hours < 0:
        self.is_time_up = True


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
                        self.list_of_labels[index_num].text = self.list_of_textInputs[i].text[0]
                        self.list_of_labels[index_num - 1].text = self.list_of_textInputs[i].text[1]
                else:
                    self.list_of_labels[index_num].text = self.list_of_textInputs[i].text[j]
            except: 
                self.list_of_labels[index_num].text = "0"
            index_num += 1