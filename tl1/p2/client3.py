import socket
import pickle

server_address = ("0.0.0.0", 8081)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

keep_working = True

# En el diccionario se deja solo la opcion que se requiere.
COMMAND = {"A": 1}

while keep_working:
    print("\n---------------------------------------------------")
    print("Ingrese un comando ([A]cumular, [S]alir)")
    comando = input()

    if comando == "A":
        print("Ingrese un valor a acumular")
        try:
            valor = int(input())
            payload = {"command": COMMAND[comando], "valor": valor}
            payload_serialized = pickle.dumps(payload)
            client.sendall(payload_serialized)
            data = client.recv(4096)
            result = pickle.loads(data)
            print(f"El valor acumulado es: {result.get('valor')}")
        except ValueError:
            print("Debe ingresar un numero")

    elif comando == "S":
        keep_working = False
        client.close()
        print("Sesion finalizada")

    else:
        print("El comando ingresado no es valido")
