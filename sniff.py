from scapy.all import *
from struct import *

#Usamos funcion sniff el cual captura los paquetes recividos
sniffer = sniff(count=1)
#for pack in sniffer:
 #   res = str(pack)
  #  ip_header = res[0:20]
    #iph = unpack('!BBHHHBBH4s4s' , pack)
   # print(iph)
####******Revisar no da continuo

#sniffer.pdfdump()
res = sniffer
#ipi= res[0:20]
auxi = res.hexdump()

ip = unpack('!BBHHHBBH4s4s',bytes(auxi))
Print("version: ", ip)
print(sniffer.show())
print("***************************************************")
print(sniffer.hexdump())

