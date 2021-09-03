import sys
from file_system import FS
from server import Server

# Adds top-level package directory.
sys.path.append("..")

# Comentar y descomentar las importaciones de los stubs para cambiar el comportamiento del servidor

from p3a import ServerStub

# from p3b import ServerStub

# from p5 import ServerStub

# from p7 import ServerStub


def main():
    stub = ServerStub(FS(), "50051")
    servidor = Server(stub)
    servidor.inicializar()


if __name__ == "__main__":
    main()