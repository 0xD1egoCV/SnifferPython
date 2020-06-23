from scapy.all import *

def menu():
         
    menu = """
              1.-Crear paquete IP
              2.-Ver datos del paquete creado
              3.-Enviar paquete"""
    print(menu)

flag = True

while flag == True:
    menu ()
    opcion = input("ingrese opcion :")
    if opcion == 1:
        crear()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        enviar()
    else:
         error() 
    

def crear():
    # En scapy al momento de manipular una paquete IP se tienen distintos valores;
    # Algunos importantes son "src y dst" que serian las direcciones ip de origen
    # Y destino para el paquete ip
    ip1 = "192.168.1.200"
    ip_destino = "192.168.1.100"
    packete = IP(src= ip1, dst= ip_destino)/TCP()

def mostrar():
    print(packete.src)
def enviar():
    send(packete)
def error():
    print("opcion invalida")
