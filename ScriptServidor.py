import socket, random


def decodificar_mensaje(mensaje):
    return mensaje.decode("utf-8")


def recibir_mensajes(conexion):
    valor_aleatorio = random.randint(0, 10)
    mensaje, cliente = conexion.recvfrom(1024)

    conexion_correcta = (valor_aleatorio < 5)
    if conexion_correcta:
        conexion.sendto(mensaje.upper(), cliente)
        detalles_solicitud = f"Se recibio una solicitud por parte de {cliente[0]}, la solicitud dice {decodificar_mensaje(mensaje)}"
        print(detalles_solicitud)


if __name__ == "__main__":
    ip = ""
    puerto = 1234
    cliente = (ip, puerto)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as socket_udp:
        socket_udp.bind(cliente)
        while True:
            recibir_mensajes(socket_udp)
