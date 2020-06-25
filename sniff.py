from scapy.all import *


#Usamos funcion sniff el cual captura los paquetes recividos
sniffer = sniff()
print(sniffer.show())
####******Revisar no da continuo