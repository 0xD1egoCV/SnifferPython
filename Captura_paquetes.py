import socket

#Creamos un socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)


# recibimos un packet
while True:
  print s.recvfrom(65535)
  