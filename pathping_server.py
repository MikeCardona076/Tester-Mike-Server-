import subprocess

class PathPingServer():
    def __init__(self, host):
        self.host = host

    def test_connection(self):
        try:
            pathping = subprocess.Popen(['pathping', self.host], stdout=subprocess.PIPE)
            output = pathping.communicate()[0]
            string_output = output.decode('utf-8')
            return string_output
        except:
            return False

    def run_test_pathping(self):
        text_body = self.test_connection()
        with open('pathping_server.txt', 'w') as f:
            f.write(text_body)
            f.write('\n')
            

'''
Que es PathPing?
Este comando proporciona información sobre la latencia de red y la pérdida en saltos intermedios entre un origen y un destino.
Este comando envía varios mensajes de solicitud de eco a cada enrutador entre un origen y un destino, 
durante un período de tiempo, y luego calcula los resultados en función de los paquetes devueltos por cada enrutador.

Debido a que este comando muestra el grado de pérdida de paquetes en cualquier enrutador o enlace determinado, 
puede determinar qué enrutadores o subredes podrían tener problemas de red.


'''