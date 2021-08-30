from stub import Stub
from client import Cliente


def main():
    stub = Stub("localhost", 8090)
    cliente = Cliente(stub)
    cliente.conectar()

    while True:
        print("> Ingrese un mensaje")
        print("> Ingrese 'salir' para salir del sistema\n")
        user_mensaje = input()
        cliente.enviar(user_mensaje)
        mensaje = cliente.recibir()
        print(f"Respuesta: {mensaje}\n")

        if user_mensaje == "salir":
            break
    cliente.desconectar()


main()