import socket
from struct import *
import datetime
import pcapy
import sys

	#list all devices
devices = pcapy.findalldevs()
#print(devices)

for device in devices:
    print(device)
dev = input("Ingrese el dispositivo que desea usar: ")
captura = pcapy.open_live(dev, 65535, 1, 0)	


num = 0
while num < 10:
    packet = captura.next()
    num = num +1
    print(packet)
    
	