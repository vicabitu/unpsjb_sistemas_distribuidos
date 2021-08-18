import socket
import pickle

server_address = ("0.0.0.0", 8081)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

while True:
    print("Server disponible!")
    connection, client_address = server.accept()
    client = ":".join(list(map(str, client_address)))
    print(f"Cliente {client}")

    while True:

        data = connection.recv(4096)

        if not data:
            break

        payload = pickle.loads(data)
        comando = payload.get("command")

        if comando == 1:
            valor = payload.get("valor")
            response = {"valor": valor}
            response_serialized = pickle.dumps(response)
            connection.sendall(response_serialized)

        else:
            print(
                f"El cliente solicito el comando {comando} con el valor {payload.get('valor')}"
            )
            break

    connection.close()
    print("cliente desconectado \n")
