from random import randint
from socket import socket, AF_INET, SOCK_DGRAM

cliente = ("", 1234)

conexion = socket(AF_INET, SOCK_DGRAM)
conexion.bind(cliente)
while True:
    valorAleatorio = randint(0, 10)
    mensaje, host = conexion.recvfrom(1024)

    conexionCorrecta = (valorAleatorio < 5)
    if conexionCorrecta:
        conexion.sendto(mensaje.upper(), host)