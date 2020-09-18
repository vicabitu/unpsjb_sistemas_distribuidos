from client import Client
from p3a import ClientStub

def main():
    stub = ClientStub('localhost', '50051')
    cliente = Client(stub)
    cliente.conectar()
    respuesta = cliente.listar_archivos('.')
    print(respuesta)

if __name__ == '__main__':
    main()