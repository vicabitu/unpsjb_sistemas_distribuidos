import socket


server_address = (('0.0.0.0', 8090))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen()

message = 'I am SERVER\n'

while True:
	print('Server disponible!')
	connection, client_address = server.accept()
	from_client = ''

	while True:
		data = connection.recv(4096)
		if not data: break
		from_client += data.decode()

		connection.send(message.encode('utf-8'))

	print(from_client)

	connection.close()
	print('cliente desconectado \n')

