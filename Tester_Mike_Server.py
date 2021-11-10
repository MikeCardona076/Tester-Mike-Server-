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


class Test_Pip(GridLayout):

    def __init__(self, **kwargs):
        super(Test_Pip, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='IP Address'))
        self.ipaddress = TextInput(multiline=False)
        self.add_widget(self.ipaddress)
        cehckbox1 = CheckBox()
        self.add_widget(Label(text='Ping'))
        self.add_widget(cehckbox1)
        cehckbox2 = CheckBox()
        self.add_widget(Label(text='Tracert'))
        self.add_widget(cehckbox2)
        cehckbox3 = CheckBox()
        self.add_widget(Label(text='Pathping'))
        self.add_widget(cehckbox3)


    def test_pin_server(self):
        ping_result = Ping(self.ipaddress.text)
        ping_result.run_test_ping()
        return ping_result



class Tester_Mike(App):
    
    def build(self):
        return Test_Pip()

if __name__ == '__main__':
    Tester_Mike().run()

    # def __init__(self, server):
    #     self.server = server
    #     self.port = 587
    #     self.process = None

    # def test_pin_server(self):
    #     ping_result = Ping(self.server)
    #     ping_result.run_test_ping()
    #     return ping_result

    # def test_tracert_server(self):
    #     tracert_result = Tracert(self.server)
    #     tracert_result.run_test_tracert()
    #     return tracert_result

    # def test_pathping_server(self):
    #     pathping_result = Pathping(self.server)
    #     pathping_result.run_test_pathping()
    #     return pathping_result
        


