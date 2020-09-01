from stub import Stub
from mock_stub import MockStub
from client import Cliente


def main():

    # definicion de los stubs stub y mock_stub
    stub = Stub('localhost', 8090)
    mock_stub = MockStub('localhost', 8090)

    # para emplear otro stub, se cambia el parametro 
    # que se le brinda a la clase Cliente
    cliente = Cliente(stub)

    cliente.conectar()

    cliente.enviar('un mensaje')
   
    mensaje = cliente.recibir()
    print(mensaje)

    cliente.desconectar()


main()
