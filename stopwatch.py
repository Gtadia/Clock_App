from kivy.clock import Clock

def Start_Stopwatch(self, state):
        if self.was_paused:
            self.miliseconds = 0
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        self.list_of_labels = [
            self.ids.time_1,
            self.ids.time_2,
            self.ids.time_3,
            self.ids.time_4,
            self.ids.time_5,    
            self.ids.time_6
            ]
        self.was_paused = False

        if state == "START":
            self.event = Clock.schedule_interval(lambda dt: get_time(self, dt), 0.05)
            self.ids.startStopButton.text = "STOP"
            self.was_paused = True
        else:
            self.event.cancel()
            self.ids.startStopButton.text = "START"


# def get_time(self, deltaTime):
#     print(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

def get_time(self, deltaTime):
    increment = 5
    self.miliseconds += (increment + deltaTime * 10)
    if self.miliseconds >= 100:
        self.seconds += 1
        self.miliseconds = 0
    if self.seconds >= 60:
        self.minutes += 1
        self.seconds = 0
    if self.minutes >= 60:
        self.hours += 1
        self.minutes = 0
    if self.hours >= 99:
        increment = 0 

    str_list = [
        str(int(self.miliseconds)),
        str(self.seconds),
        str(self.minutes)
        # str(self.hours)
        ]


    # print(f"{self.hours} : {self.minutes} : {self.seconds} : {self.miliseconds}")
    # print(deltaTime * 100)

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
