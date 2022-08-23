from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import json
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.button import Button


Main_ScrollView = ScrollView(bar_width = 12)
Main_BoxLayout = BoxLayout(size_hint = (None, None), size=(Window.width, Window.height), orientation = "vertical")
class FirstWindow(Screen):
    def add_time(self):
        timer_list = []
        
        with open("/Users/mh/Documents/Projects/Programs/Clock_App/test/test.json", 'r') as open_file:
            timer_list = json.load(open_file)


        
        # When you press the start or enlarge a timer, return alarm number/index to kivy
        for i in range(len(timer_list)):
            print("Hello")
            # Main_BoxLayout.add_widget(Button(text = "Hello"))
            min_height = 400
            width, height = Window.size
            if height < 400:
                min_height = 300
            elif height > 1000: 
                min_height = 500

            Some_BoxLayout = BoxLayout(size_hint = (None, None), size = (self.width, min_height), orientation = "horizontal")
            Some_BoxLayout.add_widget(Button(text= "Hi"))

            Main_BoxLayout.add_widget(Some_BoxLayout)
    
        Main_ScrollView.add_widget(Main_BoxLayout)
        Main_Main_BoxLayout = BoxLayout(size_hint = (1, 1))
        # Main_Main_BoxLayout.add_widget(Main_ScrollView)

        self.add_widget(Main_ScrollView)

# class Update_time(Widget):
#     print("Hello")
#     Builder.load_string("""<Update_time> 
#     BoxLayout:
#         size: root.width, root.height
#         orientation: "vertical"
#         Button: 
#             text: "Hi"
#     """)




class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class TimeCounter(Widget):
    pass


class TestApp(App):
    def buidl(self):
        return Builder.load_file("test.kv")


if __name__ == "__main__":
    TestApp().run()