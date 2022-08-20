import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

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

def Reset_Timer(self):
    self.ids.time_input_seconds = '' 
    self.ids.time_input_minutes = ''
    self.ids.time_input_hours = ''
    

def Start_Timer(self):
    self.seconds = 0
    self.minutes = 0
    self.hours = 0

    self.is_time_up = False

    self.list_of_textInputs = [
        self.ids.time_input_seconds, 
        self.ids.time_input_minutes, 
        self.ids.time_input_hours  
    ]
    list_of_max_num = [59, 59, 23]
    is_valid_format = True
        
    for i in range(3):
        if self.list_of_textInputs[i].text != '':
            if int(self.list_of_textInputs[i].text) > list_of_max_num[i]:
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



    if self.ids.Timer_StartStopButton == "START":
        Clock.schedule_interval(self.get_time, 1)
        self.ids.Timer_StartStopButton.text = "STOP"
    
    if self.is_time_up:
        Clock.unschedule(self.get_time)
        self.ids.Timer_StartStopButton.text = "START"




def get_time(self, deltaTime):
    increment = 1
    self.miliseconds += (increment + deltaTime)
    if self.seconds >= 60:
        self.minutes += 1
        self.seconds = 0
    if self.minutes >= 60:
        self.hours += 1
        self.minutes = 0
    if self.hours >= 99:
        increment = 0 


    # print(f"{self.hours} : {self.minutes} : {self.seconds} : {self.miliseconds}")
    # print(deltaTime * 100)

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