import socket


class Stub:

    def __init__(self, host='0.0.0.0', port=8080):
       self.host = host
       self.port = port

    def conectar(self):
       self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.client.connect((self.host, self.port))

    def desconectar(self):
       self.client.close()

    def enviar(self, message):
       self.client.send(message.encode('utf-8'))

    def recibir(self):
       msg = self.client.recv(4096)
       return msg if not type(msg) == bytes else msg.decode()
