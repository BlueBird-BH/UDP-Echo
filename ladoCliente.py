from time import time
from socket import socket, timeout, AF_INET, SOCK_DGRAM


class Ping:
    def __init__(self, host, puerto):
        self.servidor = (host, puerto)
        self.conexion = socket(AF_INET, SOCK_DGRAM)
        self.conexion.settimeout(1)

    def ping(self):
        mensajeEnviado = "Ping"
        tiempoInicial = time()
        self.conexion.sendto(mensajeEnviado.encode("utf-8"), self.servidor)

        try:
            mensajeRecibido = self.conexion.recvfrom(1024)[0].decode("utf-8")
            tiempoFinal = time()
            tiempoTotal = self.calcularTiempo(tiempoInicial, tiempoFinal)
            return {
                "Mensaje recibido": mensajeRecibido,
                "Tiempo": f"{tiempoTotal} segundos"
            }
        except timeout:
            return {"Tiempo": "Solicitud expirada"}

    def calcularTiempo(self, inicial, final):
        tiempoTranscurrido = final - inicial
        return round(tiempoTranscurrido, 5)

    def cerrarConexion(self):
        self.conexion.close()


if __name__ == "__main__":
    ip = input("Ingrese la dirección IP del servidor: ")
    cantidadSecuencias = input("Ingrese la cantidad de solicitudes a enviar: ")
    cantidadSecuencias = int(cantidadSecuencias) + 1

    for secuencia in range(1, cantidadSecuencias):
        ping = Ping(ip, 1234)
        datosSolicitud = ping.ping()
        print(f"Secuencia No. {secuencia}, {datosSolicitud['Tiempo']}")
        ping.cerrarConexion()
