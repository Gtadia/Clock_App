import re
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
import json
from normal_rounding import Round

def text_inputted(self):
    timer_dict = dict()
    timer_keys = ["seconds", "minutes", "hours"]

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
    
        try:
            if self.list_of_textInputs[i].text == '':
                timer_dict[timer_keys[i]] = 0
            else:
                timer_dict[timer_keys[i]] = int(self.list_of_textInputs[i].text)
        except:
            timer_dict[timer_keys[i]] = 0

        with open("timer.json", "w") as open_file:
            open_file.write(json.dumps(timer_dict, indent=4))

        list_of_time = []
        with open("timer.json", "r") as open_file:
            for value in json.load(open_file).values():
                list_of_time.append(str(value))

        # print(list_of_time[i])
        for j in range(2):
            try:
                if len(list_of_time[i]) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num].text = list_of_time[i][0]
                        self.list_of_labels[index_num - 1].text = list_of_time[i][1]
                else:
                    self.list_of_labels[index_num].text = list_of_time[i][j]
            except: 
                self.list_of_labels[index_num].text = "0"
            index_num += 1


def Start_Timer(self):
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

    if self.ids.Timer_StartStopButton.text == "START":
        self.event = Clock.schedule_interval(lambda dt: get_time(self, dt), 1)
        self.ids.Timer_StartStopButton.text = "STOP"
    else: 
        self.event.cancel()
        self.ids.Timer_StartStopButton.text = "START"


def Reset_Timer(self):
    self.ids.time_input_seconds.text = '' 
    self.ids.time_input_minutes.text = ''
    self.ids.time_input_hours.text = ''
    self.event.cancel()
    self.ids.Timer_StartStopButton.text = "START"

    index_num = 0
    for i in range(len(self.list_of_textInputs)):
        for j in range(2):
            self.list_of_labels[index_num].text = "0"
            index_num += 1


def get_time(self, deltaTime):
    timer_list = []
    with open("timer.json", "r") as open_file:
        for value in json.load(open_file).values():
            timer_list.append(value)

    increment = 1
    timer_list[0] = timer_list[0] - increment * deltaTime
    if timer_list[0] <= timer_list[1] == timer_list[2] == 0:
        for i in range(len(self.list_of_textInputs)):
            self.list_of_textInputs[i].text = ''
        print('STOP')
        self.ids.Timer_StartStopButton.text = "START"
        self.event.cancel()
    else:
        print("hello?")
        if timer_list[0] < -0.5:
            print("1")
            timer_list[1] -= 1
            timer_list[0] = 59
        if timer_list[1] <= -0.5:
            print("2")
            timer_list[2] -= 1
            timer_list[1] = 59
        if timer_list[2] < -0.5: 
            print("3")
            increment = 0

    

    with open("timer.json", "w") as open_file:
        open_file.write(
            json.dumps(
            {"seconds": timer_list[0], 
            "minutes": timer_list[1],
            "hours": timer_list[2]
            }, indent=4)
        )

    print(timer_list)



    print(deltaTime)

    index_num = 0
    for i in range(len(timer_list)):
    # Add hours label widget when we get there (try not to have it there when we don't need it)

        for j in range(2):
            rounded_time = str(Round().round(timer_list[i]))
            try:
                if len(rounded_time) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num].text = rounded_time[0]
                        self.list_of_labels[index_num - 1].text = rounded_time[1]
                else:
                    self.list_of_labels[index_num].text = rounded_time[j]
            except: 
                self.list_of_labels[index_num].text = "0"
            index_num += 1