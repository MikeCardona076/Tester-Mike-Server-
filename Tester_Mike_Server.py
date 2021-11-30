import time
import os 
from  ping_server import PingServer as Ping
from tracert_server import  TracertServer as Tracert
from pathping_server import PathPingServer as Pathping
from sendemail_server import SendEmail as Sendemail
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox



class Pip_Eternal(GridLayout): 
    def __init__(self, **kwargs):
        super(Pip_Eternal, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='IP Address'))
        self.ipaddress = TextInput(multiline=False)
        self.ping = Ping(self.ipaddress.text)

    def run(self):
        while True:
            os.system('cls')
            self.add_widget(Label(text=self.ping.test_connection()))
            time.sleep(1)
            


class Test_Pip(GridLayout):

    def __init__(self, **kwargs):
        super(Test_Pip, self).__init__(**kwargs)
        try:
            self.cols = 2
            self.add_widget(Label(text='IP Address'))
            self.ipaddress = TextInput(multiline=False)
            self.add_widget(self.ipaddress)
            self.checkbox1 = CheckBox()
            self.add_widget(Label(text='Ping'))
            self.add_widget(self.checkbox1)
            self.checkbox2 = CheckBox()
            self.add_widget(Label(text='Tracert'))
            self.add_widget(self.checkbox2)
            self.checkbox3 = CheckBox()
            self.add_widget(Label(text='Pathping'))
            self.add_widget(self.checkbox3)
            button = Button(text='Test', font_size=40)
            self.add_widget(button)
            button.bind(on_press=self.test_pin_server)
            button = Button(text='Close', font_size=40)
            self.add_widget(button)
            button.bind(on_press=self.clear_all)
        except Exception as e:
            print(e)
            print('Error')


    def test_pin_server(self, instance):
        if self.checkbox1.active:
            ping = Ping(self.ipaddress.text)
            ping.run_test_ping()
        if self.checkbox2.active:
            tracert = Tracert(self.ipaddress.text)
            tracert.run_test_tracert()
        if self.checkbox3.active:
            pathping = Pathping(self.ipaddress.text)
            pathping.run_test_pathping()
        return True
        
    def clear_all(self):
        self.ipaddress.text = ''
        self.checkbox1.active = False
        self.checkbox2.active = False
        self.checkbox3.active = False
        return True



    
class Tester_Mike(App):
    
    def build(self):
        return Test_Pip()

if __name__ == '__main__':
    Tester_Mike().run()
