import socket, sys
from struct import*

#Creamos un socket para recivir paquetes de tipo TCP
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

contador = 1


def whatflag(flags):
  if flags == 16384:
    return "No Divisible"
  else: 
    return "Divisible"

# recibimos 10 paquetes
while contador <=100:
  packet = s.recvfrom(65535)
  packet = packet[0]

  info_ip = packet[0:20]
  cabecera_ip = unpack('!BBHHHBBH4s4s' , info_ip)

  version_IHL = cabecera_ip[0]
  version = version_IHL >> 4
  ihl = version_IHL & 0xF
  longitud_iph = ihl*4  

  tos = cabecera_ip[1]
  longitud_total = cabecera_ip[2]
  ip_id = cabecera_ip[3]
  flags = cabecera_ip[4]
  ttl = cabecera_ip[5]
  protocolo = cabecera_ip[6]
  checksum = cabecera_ip[7]
  ip_origen =  socket.inet_ntoa(cabecera_ip[8])
  ip_destino = socket.inet_ntoa(cabecera_ip[9])
  print('##########################################################################################')
  print("Datos recividos: ",packet)
  
  print('version de IP: ' + str(version))         #1
  print('IHL: ' +str(ihl)+ ' es decir: '+ str(ihl*32//8) + ' bytes')                       #1
  print('TOS: ' + str(tos))                       #2
  print('IP Total Length: '+ str(longitud_total)+' es decir: '+ str(longitud_total*32//8)+ ' bytes') #3
  print('ID: '+ str(ip_id))                            #4
  #print('Flags :' + str(flags)) +" "+ whatflag(flags)                      #5
  print('TTL: ' + str(ttl))                       #6
  print('Protocolo: ' + str(protocolo))           #7
  print('Cheksum: '+ str(checksum))               #8
  print('IP origen: '+ str(ip_origen))            #9
  print('IP destino '+ str(ip_destino))           #10
  
  print("**************INFORMACION DE TCP********************")
  # ahora para la parte de TCP
  info_tcp = packet[longitud_iph:longitud_iph+20]
  cabecera_tcp = unpack('!HHLLBBHHH',info_tcp)
  puerto_orig = cabecera_tcp[0]
  puerto_dest = cabecera_tcp[1]
  num_seq = cabecera_tcp[2]
  ack_num = cabecera_tcp[3]
  data_offset = cabecera_tcp[4]
  flagsTCP = cabecera_tcp[5]
  win_size = cabecera_tcp[6]
  checksumTCP = cabecera_tcp[7]
  longitud_tcph = data_offset >> 4
  urg_p = cabecera_tcp[8]
  print('Puerto Origen:  '+ str(puerto_orig))
  print('Puerto Destino: '+ str(puerto_dest))
  print('Numero Secuencia:  '+ str(num_seq))
  print('Acknowledgment: '+ str(ack_num))
  print('Data offset: '+ str(data_offset))
  print('Longitud cabecera TCP: '+ str(longitud_tcph)+ ' es decir '+ str(longitud_tcph*32//8) + ' bytes' )
  print('Flags de TCP: '+ str(flagsTCP))
  print('Window Size: '+ str(win_size))
  print('Checksum: ' + str(checksumTCP))
  print('Urgent Pointer:'+str(urg_p))
  
  # Datos recividos
  longitud_cab = longitud_iph + longitud_tcph *4
  longitud_datos = len(packet) - longitud_cab
  datos = packet[longitud_cab:]
  print('DATOS: ',(datos))


  contador = contador + 1