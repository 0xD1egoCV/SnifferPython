import socket, sys
from struct import*

#Creamos un socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)


# recibimos un packet
while True:
  packet = s.recvfrom(65535)
  packet = packet[0]

  info_ip = packet[0:20]
  ip_f = unpack('!BBHHHBBH4s4s' , info_ip)
  version = ip_f[0]
  ttl = ip_f[5]
  protocolo = ip_f[6]

  print 'version: '+str(version)
  print 'TTL: ' + str(ttl)
  print 'Protocolo: ' + str(protocolo)