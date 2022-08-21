from kivy.clock import Clock
import json

def Start_Stopwatch(self, state):
    self.list_of_labels = [
        self.ids.time_1,
        self.ids.time_2,
        self.ids.time_3,
        self.ids.time_4,
        self.ids.time_5,    
        self.ids.time_6
        ]

    if state == "START":
        self.event = Clock.schedule_interval(lambda dt: get_time(self, dt), 0.05)
        self.ids.startStopButton.text = "STOP"

    else:
        self.event.cancel()
        self.ids.startStopButton.text = "START"


# def get_time(self, deltaTime):
#     print(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

def get_time(self, deltaTime):
    with open("stopwatch.json", "r") as file_data:
        self.stopwatch_data = json.load(file_data)


    increment = 5
    self.stopwatch_data["miliseconds"] = self.stopwatch_data["miliseconds"] + (increment + deltaTime)
    if self.stopwatch_data["miliseconds"] >= 100:
        self.stopwatch_data["seconds"] += 1
        self.stopwatch_data["miliseconds"] = 0
    if float(self.stopwatch_data["seconds"]) >= 60:
        self.stopwatch_data["minutes"] += 1
        self.stopwatch_data["seconds"] = 0
    if float(self.stopwatch_data["minutes"]) >= 60:
        self.stopwatch_data["hours"] += 1
        self.stopwatch_data["minutes"] = 0
    if float(self.stopwatch_data["hours"]) >= 99:
        increment = 0 
        
    with open("stopwatch.json", "w") as file_data:
        file_data.write(json.dumps(self.stopwatch_data, indent = 4))

    print(self.stopwatch_data)




#     # print(f"{self.hours} : {self.minutes} : {self.seconds} : {self.miliseconds}")
#     # print(deltaTime * 100)
    str_list = [
        str(int(self.stopwatch_data["miliseconds"])),
        str(self.stopwatch_data["seconds"]),
        str(self.stopwatch_data["minutes"])
    ]


    index_num = 0
    for i in range(len(str_list)):        
    # Add hours label widget when we get there (try not to have it there when we don't need it)
        for j in range(2):
            try:
                if len(str_list[i]) == 2:
                    if j == 1:  
                        # Switches the last digit's location with the first digit's location
                        self.list_of_labels[index_num].text = str_list[i][0]
                        self.list_of_labels[index_num - 1].text = str_list[i][1]
                else:
                    self.list_of_labels[index_num].text = str_list[i][j]
            except: 
                self.list_of_labels[index_num].text = "0"
            index_num += 1