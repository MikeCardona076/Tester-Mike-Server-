import subprocess

class TracertServer():
    def __init__(self, host):
        self.host = host

    def test_connection(self):
        try:
            pathping = subprocess.Popen(['tracert', self.host], stdout=subprocess.PIPE)
            output = pathping.communicate()[0]
            string_output = output.decode('utf-8')
            return string_output
        except:
            return False

    def run_test_tracert(self):
        text_body = self.test_connection()
        with open('tracert_server.txt', 'w') as f:
            f.write(text_body)
            f.write('\n')
            

'''
Que es un tracert?
Esta es una de las principales herramientas de diagnóstico que determina la ruta tomada a un destino mediante el envío de solicitudes 
de eco del protocolo ICMP o mensajes ICMPv6 al destino con valores de campo de tiempo de vida (TTL) que se mantienen incrementando.

Cada enrutador a lo largo de la ruta debe disminuir el TTL en un paquete IP en al menos 1 antes de reenviarlo. 
Efectivamente, el TTL es un contador de enlaces máximo. Cuando el TTL de un paquete llega a 0, 
se espera que el enrutador devuelva un mensaje de tiempo ICMP excedido a la computadora de origen.

Este comando determina la ruta enviando el primer mensaje de solicitud de eco con un TTL de 1 e incrementando el TTL en 1 en cada transmisión subsiguiente hasta que el objetivo responda o se alcance el número máximo de saltos. 
El número máximo de saltos es 30 de forma predeterminada y se puede especificar mediante el parámetro /h .


'''



# numpolunico  idpoliz
# SC0100001	    3
# SC0100002	    6
# SI0000004	    1
# SI0000008   	2
# SI0000009   	4
# SI0000005    	5
# SI0000006	    7
# SI0000007	    8
# SI0000003	    9
# SI0000002	    10





'''



UPDATE FACTURAS SET fecvenc = to_date('26-08-2021', 'DD/MM/YYYY') WHERE idfactura= 6;


UPDATE FACTURAS SET fecvenc = to_date('04-08-2020', 'DD/MM/YYYY') WHERE idfactura= 25;


UPDATE FACTURAS SET fecvenc = to_date('02-05-2018', 'DD/MM/YYYY') WHERE idfactura= 1;


UPDATE FACTURAS SET fecvenc = to_date('24-03-2019', 'DD/MM/YYYY') WHERE idfactura= 2;

UPDATE FACTURAS SET fecvenc = to_date('26-09-2020', 'DD/MM/YYYY') WHERE idfactura= 4;


UPDATE FACTURAS SET fecvenc = to_date('27-09-2018', 'DD/MM/YYYY') WHERE idfactura= 5;


UPDATE FACTURAS SET fecvenc = to_date('20-10-2021', 'DD/MM/YYYY') WHERE idfactura= 7;
UPDATE FACTURAS SET fecvenc = to_date('20-04-2022', 'DD/MM/YYYY') WHERE idfactura= 8;


UPDATE FACTURAS SET fecvenc = to_date('20-10-2021', 'DD/MM/YYYY') WHERE idfactura= 9;
UPDATE FACTURAS SET fecvenc = to_date('20-01-2022', 'DD/MM/YYYY') WHERE idfactura= 10;
UPDATE FACTURAS SET fecvenc = to_date('20-04-2022', 'DD/MM/YYYY') WHERE idfactura= 11;
UPDATE FACTURAS SET fecvenc = to_date('20-07-2022', 'DD/MM/YYYY') WHERE idfactura= 12;



UPDATE FACTURAS SET fecvenc = to_date('30-06-2019', 'DD/MM/YYYY') WHERE idfactura= 13;
UPDATE FACTURAS SET fecvenc = to_date('31-08-2019', 'DD/MM/YYYY') WHERE idfactura= 14;
UPDATE FACTURAS SET fecvenc = to_date('31-10-2019', 'DD/MM/YYYY') WHERE idfactura= 15;
UPDATE FACTURAS SET fecvenc = to_date('31-12-2019', 'DD/MM/YYYY') WHERE idfactura= 16;
UPDATE FACTURAS SET fecvenc = to_date('29-02-2020', 'DD/MM/YYYY') WHERE idfactura= 17;
UPDATE FACTURAS SET fecvenc = to_date('30-04-2020', 'DD/MM/YYYY') WHERE idfactura= 18;


UPDATE FACTURAS SET fecvenc = to_date('30-06-2017', 'DD/MM/YYYY') WHERE idfactura= 19;
UPDATE FACTURAS SET fecvenc = to_date('31-08-2017', 'DD/MM/YYYY') WHERE idfactura= 20;
UPDATE FACTURAS SET fecvenc = to_date('31-10-2017', 'DD/MM/YYYY') WHERE idfactura= 21;
UPDATE FACTURAS SET fecvenc = to_date('31-12-2017', 'DD/MM/YYYY') WHERE idfactura= 22;
UPDATE FACTURAS SET fecvenc = to_date('28-02-2018', 'DD/MM/YYYY') WHERE idfactura= 23;
UPDATE FACTURAS SET fecvenc = to_date('30-04-2018', 'DD/MM/YYYY') WHERE idfactura= 24;



'''