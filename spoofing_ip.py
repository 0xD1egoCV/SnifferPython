#NOTA: funciona con python 3.7 y 3.8
from scapy.all import *
class spoofing:
	def __init__(self, ip_origen, ip_destino):
		self.ip_origen = ip_origen
		self.ip_destino = ip_destino

def crear(origin, destiny,protocolo):
	if protocolo == 1:
		res = IP(src=origin, dst= destiny)/TCP()
		
		print("packete TCP creado ")
	elif protocolo == 2:
		res = IP(src=origin, dst= destiny)/ICMP()
		print("packete ICMP creado ")
	elif protocolo == 3:
		res = IP(src=origin, dst= destiny)/UDP()
		print("packete UDP creado ")
	else : print("opcion invalida")
	
	return res
def mostrar(aux):
	print("IP de origen: ", aux.src)
	print("IP destino: ", aux.dst)

def enviar(packete):
	payload = input("Ingrese carga util >>")
	aux = packete/payload
	send(aux)
	print("Paquete enviado")
	

def nada():
	print("Opcion invalida")

def showProtocol():
	print("""1.- TCP
			2.- ICMP
			3.- UDP""")

def prot(opcion):
	if opcion == 1:
		return "TCP"
	elif opcion == 2:
		return "ICMP"
	elif opcion == 3:
		return "UDP"

menu = """
    1.-Crear paquete IP
    2.-Ver datos del paquete creado
    3.-Enviar paquete"""


flag = True
while flag == True:
	print(menu)
	opcion = int(input("Ingrese la opcion >> "))
	if opcion == 1:
		ip_or = input("Ingrese IP origen >> ")
		ip_des = input("Ingrese IP destino >>")
		showProtocol()
		protocolo = int(input("Seleccione el protocolo: "))
		aux = crear(ip_or, ip_des, protocolo)
		
	elif opcion == 2:
		mostrar(aux)
	elif opcion == 3:
		enviar(aux)
	else : nada()
