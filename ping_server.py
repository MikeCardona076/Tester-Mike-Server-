import subprocess

class PingServer():
    def __init__(self, host):
        self.host = host

    def test_connection(self):
        try:
            pathping = subprocess.Popen(['ping', self.host], stdout=subprocess.PIPE)
            output = pathping.communicate()[0]
            string_output = output.decode('utf-8')
            return string_output
        except:
            return False

    def run_test_ping(self):
        text_body = self.test_connection()
        with open('ping_server.txt', 'w') as f:
            f.write(text_body)
            f.write('\n')
            
"""
Que es un ping?
Siempre que necesites hacer una verificación sobre un dispositivo interconectado en una infraestructura de red se encuentra 
levantado o no, la primera prueba básica debe ser lanzar una consulta al protocolo de red ICMP (Internet Control Message Protocol)
 en una red de tipo TCP/IP (Protocolo de Control de Transmisión / Protocolo de Internet).

Ping es un acrónimo de Packet Internet Groper que en español se traduce a un buscador de paquetes en redes.

Aunque la mayoría de los usuarios que aplican un uso básico de la consola, usan este comando para saber si existe conectividad
 a internet.

"""