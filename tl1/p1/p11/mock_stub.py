import socket
from collections import namedtuple


class MockStub:

    def __init__(self, host='0.0.0.0', port=8080):
       self.host = host
       self.port = port

    def conectar(self):
        print('Client connected')

    def desconectar(self):
       print('Client disconnected')

    def enviar(self, message):
       self.message = message

    def recibir(self):       
       return self.message
