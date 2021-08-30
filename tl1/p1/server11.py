from srv_stub import Stub
from server import Server


def main():

    try:
        stub = Stub("0.0.0.0", 8090)
        server = Server(adapter=stub)
        server.config()
        server.start()
        print("Server disponible!")
        while True:
            server.accept_connection()
            # Show client
            print("> ", server.get_client())
            # Echoing message
            message = server.receive()
            print(f"> Message received: {message}")

            while message != "salir":
                server.send(message)
                message = server.receive()
                print(f"> Message received: {message}")
            server.send(message)
            print(f"> Client disconnected \n")
    except KeyboardInterrupt:
        print(f"> Server disconnected \n")
        server.close_socket()


if __name__ == "__main__":
    main()