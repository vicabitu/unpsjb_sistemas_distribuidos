from stub import Stub
from mock_stub import MockStub
from client import Cliente


def main():
    # import pdb

    # definicion de los stubs stub y mock_stub
    stub = Stub("localhost", 8090)
    mock_stub = MockStub("localhost", 8090)

    # para emplear otro stub, se cambia el parametro
    # que se le brinda a la clase Cliente
    cliente = Cliente(stub)
    # pdb.set_trace()
    cliente.conectar()

    while True:
        print("Ingrese un mensaje")
        user_mensaje = input()

        cliente.enviar(user_mensaje)

        mensaje = cliente.recibir()
        print(f"Respuesta: {mensaje}")

        if user_mensaje == "salir":
            break

    cliente.desconectar()


main()