import socket, time


def codificar_mensaje(mensaje):
    return mensaje.encode("utf-8")


def decodificar_mensaje(mensaje):
    return mensaje.decode("utf-8")


def calcular_tiempo(tiempo_inicial, tiempo_final):
    tiempo_total = round(tiempo_final - tiempo_inicial, 5)
    return f"{tiempo_total} milisegundos"


def enviar_mensaje(mensaje, servidor):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_udp:
        socket_udp.settimeout(1)

        socket_udp.sendto(codificar_mensaje(mensaje), servidor)
        tiempo_inicial = time.time()

        try:
            respuesta = decodificar_mensaje(socket_udp.recvfrom(1024)[0])
            tiempo_final = time.time()
            tiempo_respuesta = calcular_tiempo(tiempo_inicial, tiempo_final)

            return respuesta, tiempo_respuesta
        except socket.timeout:
            return "No se recibió respuesta", "Tiempo excedido"


if __name__ == "__main__":
    ip = input("Ingrese la IP del servidor: ")
    cantidad_secuencias = int(input("Ingrese la cantidad de secuencias: "))

    puerto = 1234
    servidor = (ip, puerto)

    for numero_secuencia in range(1, cantidad_secuencias + 1):
        mensaje = f"Ping no. {numero_secuencia}"
        respuesta, tiempo_respuesta = enviar_mensaje(mensaje, servidor)
        detalles_solicitud = f"Se envio: {mensaje}, se recibio: {respuesta}, tardo: {tiempo_respuesta}"
        print(detalles_solicitud)
