#other imports
from api import *
from plots import count, summary_graph, splitted_graph, generate_single_graphs
from vulcan._utils import VulcanAPIException
from files import create_files, reset, subjects
from os import system, listdir

#kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

#size set
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')
Config.write()


class LoginWindow(Screen):

    password_warn_label = ObjectProperty(None)
    password_input = ObjectProperty(None)
    log_in_button = ObjectProperty(None)
    new_acc_btn = ObjectProperty(None)

    def show_popup(self, title, text):
        show = PopupContent(text)
        popupWindow = Popup(title = title, content = show, size_hint= (None,None), size = (600,250))
        popupWindow.open()

    def log_in_btn_pressed(self):

        try: 
            f = open("password.txt","r")
        
            if self.password_input.text == f.read():
                f.close()
                sm.current = "GradesWindow"
            
            else: 
                self.password_warn_label.text = "Wrong password!"

        except FileNotFoundError: 
            self.password_warn_label.text = "No account!"
            self.show_popup("Warning","You have no account...\nClick 'new acc' button to create new account!")


class InfoWindow(Screen):
    
    info_textbox = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(InfoWindow, self).__init__(**kwargs)

        with open('img/info.txt', 'r') as file:
            self.info_textbox.text = file.read()


class NewAccWindow(Screen):

    warned = False

    token_input = ObjectProperty(None)
    symbol_input = ObjectProperty(None)
    pin_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    
    def reset(self):
        self.token_input.text = ""
        self.symbol_input.text = ""
        self.pin_input.text = ""
        self.password_input.text = ""

    def show_popup(self, title, text):
        show = PopupContent(text)
        popupWindow = Popup(title = title, content = show, size_hint= (None,None), size = (600,250))
        popupWindow.open()

    def create_btn_pressed(self):

        if (os.path.isfile("cert.json")) and (self.warned == False):
            self.warned = True
            self.show_popup("WARNING", "You have already connected an account!\nYou can create new one but old one will be deleted.")

        elif ((self.token_input.text == "") or 
        (self.symbol_input.text == "") or 
        (self.pin_input.text == "") or 
        (len(self.password_input.text) != 4)):

            self.show_popup("ERROR", "You left some of the text fields blank or\nyour password is not 4-digit.")

        else:
            try:
                if os.path.isfile("password.txt"): os.remove("password.txt")
                new_acc(self.token_input.text, self.symbol_input.text, self.pin_input.text)
                file = open("password.txt","w")
                file.write(self.password_input.text)
                file.close()
                self.reset()
                self.show_popup("Connected successfully!","Your Vulcan account is connected now.\nLet's log in!")
                sm.current = "LoginWindow"

            except VulcanAPIException:
                self.show_popup("ERROR", "You have no internet connection or \nyou have used invalid token, symbol, pin or password.")
                self.reset()
        

class GradesWindow(Screen):

    show_splittedgraph_btn = ObjectProperty(None)
    show_summarygraph_btn = ObjectProperty(None)
    show_averagegraph_btn = ObjectProperty(None)
    subject_grades_graph = ObjectProperty(None)
    subject_name_label = ObjectProperty(None)

    index = 0

    def on_pre_enter(self):
        fill_subjects_list()
        create_files()
        reset()
        update_grades()
        generate_single_graphs()
        
        self.subject_name_label.text = subjects[self.index]
        self.subject_grades_graph.source = f"img/{subjects[self.index]}.jpg"
        self.subject_grades_graph.reload()

    def left_swap(self):
        if self.index !=0: 

            self.index -= 1    
            self.subject_name_label.text = subjects[self.index]
            self.subject_grades_graph.source = f"img/{subjects[self.index]}.jpg"
            self.subject_grades_graph.reload()

    def right_swap(self):
        if self.index != len(subjects) - 1: 

            self.index += 1
            self.subject_name_label.text = subjects[self.index]
            self.subject_grades_graph.source = f"img/{subjects[self.index]}.jpg"
            self.subject_grades_graph.reload()

    def show_splittedgraph_btn_pressed(self):
        count()
        splitted_graph()
        
    def show_summarygraph_btn_pressed(self):
        count()
        summary_graph()

    def show_averagegraph_btn_pressed(self):
        prepare_average_grade_graph()


class MessagesWindow(Screen):
    msg_textbox = ObjectProperty(None)
    messages = []
    index = len(messages) - 1

    def on_pre_enter(self):
        update_mailbox()
        self.messages = listdir("messages")
        
        if len(self.messages) != 0: 
            with open(f"messages/{self.messages[self.index]}", 'r') as file:
                self.msg_textbox.text = file.read() 
                self.msg_textbox.cursor = (0,0)

    def left_swap(self):
        if ((len(self.messages) != 0) and (self.index != 0)): 
            self.index -= 1
            with open(f"messages/{self.messages[self.index]}", 'r') as file:
                self.msg_textbox.text = file.read() 
                self.msg_textbox.cursor = (0,0)

    def right_swap(self):
        if ((len(self.messages) != 0) and (self.index != len(self.messages) - 1)): 
            self.index += 1
            with open(f"messages/{self.messages[self.index]}", 'r') as file:
                self.msg_textbox.text = file.read()
                self.msg_textbox.cursor = (0,0) 


class PlanWindow(Screen):

    plan_textbox = ObjectProperty(None)
    day_name_label = ObjectProperty(None)

    days = []
    index = 0

    def on_pre_enter(self):
        prepare_plan() 
        self.days = listdir("plan")
        
        with open(f"plan/{self.days[self.index]}", 'r') as file:
            self.plan_textbox.text = file.read() 
            self.plan_textbox.cursor = (0,0)
            self.day_name_label.text = self.days[self.index][:-4]

    def left_swap(self):
        if self.index != 0: 
            self.index -= 1
            with open(f"plan/{self.days[self.index]}", 'r') as file:
                self.plan_textbox.text = file.read() 
                self.plan_textbox.cursor = (0,0)
                self.day_name_label.text = self.days[self.index][:-4]

    def right_swap(self):
        if self.index != 4: 
            self.index += 1
            with open(f"plan/{self.days[self.index]}", 'r') as file:
                self.plan_textbox.text = file.read() 
                self.plan_textbox.cursor = (0,0)
                self.day_name_label.text = self.days[self.index][:-4]

class ExamsWindow(Screen):
    exams_textbox = ObjectProperty(None)

    def on_pre_enter(self):
        prepare_exams()
        with open('exams.txt', 'r') as file:
            self.exams_textbox.text = file.read()

class WindowManager(ScreenManager):
    pass


class PopupContent(FloatLayout):

    information = ObjectProperty(None)

    def __init__(self, text, **kwargs):
        super(PopupContent, self).__init__(**kwargs)
        self.information.text = text


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [
    LoginWindow(name =  "LoginWindow"),
    InfoWindow(name =   "InfoWindow"),
    NewAccWindow(name = "NewAccWindow"),
    GradesWindow(name = "GradesWindow"),
    MessagesWindow(name = "MessagesWindow"),
    PlanWindow(name = "PlanWindow"),
    ExamsWindow(name = "ExamsWindow")
]


for screen in screens: sm.add_widget(screen)
sm.current = "LoginWindow"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
