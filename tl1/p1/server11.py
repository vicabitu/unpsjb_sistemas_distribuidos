from srv_stub import Stub
from server import Server


def main():

    try:
        stub = Stub("0.0.0.0", 8090)

        server = Server(adapter=stub)

        server.config()

        server.start()
        print("Server disponible!")

        print(server.adapter.server)
        server.accept_connection()
        while True:

            # Show client
            print(">    ", server.get_client())

            # Echoing message
            message = server.receive()
            print(f">    Message received: {message}")

            while message != "salir":
                server.send(message)
                message = server.receive()
                print(f">    Message received: {message}")
            server.send(message)
            server.close_connection()
            print(f">    Client disconnected \n")

    except KeyboardInterrupt:
        server.close_socket()
        print(f">    Client disconnected \n")


if __name__ == "__main__":
    main()