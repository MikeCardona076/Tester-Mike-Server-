import subprocess
import time
import smtplib 
from email.message import EmailMessage
from typing import Counter

class Tester_Mike():
    def __init__(self, server, notificacion):
        self.correo = 'mcardonaexcel@gmail.com'
        self.passw = 'snnybjmknlknybtj'
        self.notificacion = notificacion
        self.server = server
        self.port = 587
        self.process = None

    def ping_server(self):

        response = subprocess.call(['ping', self.server])
        if response == 0:
            return True
        else:
            return False
    
    def is_server_running(self):
        try:
            self.process = subprocess.check_output(['netstat', '-a'])
            return True
        except:
            return False

    def send_email(self):
        msg = EmailMessage()
        mensaje = 'Notificacion de servidor'
        msg['Subject']= mensaje
        msg['From']= self.correo
        msg['To']= self.notificacion
        cuerpo_mensaje = '''
        Hola,
        El servidor {} esta caido.
        '''.format(self.server)
        msg.set_content(cuerpo_mensaje)
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.correo, self.passw)
        s.sendmail(self.correo, self.notificacion, msg.as_string())
        s.quit()

    def start(self):
        if self.ping_server():
            if self.is_server_running():
                print('''
                ################################################
                #                                              #
                #   El servidor esta funcionando correctamente #
                #                                              #
                ################################################
                ''')
                print(time.ctime())
        else:
            print('''
            ##################################################
            #                                                #
            #  El servidor no esta funcionando correctamente #
            #                                                #
            ##################################################
            ''')
            print(time.ctime())
            self.send_email()
   

            print('''
            ################################################
            #                                              #
            #   Se ha enviado un correo de notificacion    #
            #                                              #
            ################################################
            ''')

print('''
###############################################################################
#                                                                             #
#             Bienvenido al programa de prueba de servidores                  #
#                               Por Mike Cardona                              #
#                               Version: 1.0                                  #
#                                 10/20/2021                                  #
#                                                                             #
###############################################################################
''')

servidor = input('Ingrese la Ip publica del servidor: ')
try: 
    notificacion = input('Ingrese el correo electronico para enviar notificacion: ')
    

except:
    print('Error')

server = Tester_Mike(servidor, notificacion)
server.start()
tester_mike = Tester_Mike(servidor, notificacion)

while True:
    tester_mike.start()
    time.sleep(5)
    print('\n')

