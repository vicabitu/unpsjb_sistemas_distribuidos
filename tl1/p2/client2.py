import socket
import random

from structures import payload_X

server_address = ('0.0.0.0', 8081)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

keep_working = True
client_id = random.randint(100000, 999999)

COMMAND = {'A': 1, 'O': 2}

while keep_working:
	print('\n---------------------------------------------------')
	print('Ingrese un comando ([A]cumular, [O]btener, [S]alir)')
	comando = input()

	if comando == 'A':
		print('Ingrese un valor a acumular')
		valor = int(input())
		payload = payload_X(client_id, COMMAND[comando], valor)
		client.sendall(payload)

	elif comando == 'O':
		payload = payload_X(client_id, COMMAND[comando], 0)
		client.sendall(payload)
		data = client.recv_into(payload)
		print(f'El valor acumulado es: {payload.data}')

	elif comando == 'S':
		keep_working = False
		client.close()
		print('Sesion finalizada')	

	else:
		print('El comando ingresado no es valido')
