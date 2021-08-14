import socket


class Stub:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.connection = None
        self.client = None

    def config(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def start(self):
        self.server.listen()

    def accept_connection(self):
        self.connection, self.client = self.server.accept()
        self.client = ":".join(list(map(str, self.client)))

    def close_connection(self):
        self.connection.close()
        self.connection = None
        self.client = None

    def send(self, message):
        self.connection.send(message.encode("utf-8"))

    def receive(self):
        msg = self.connection.recv(4096)
        return msg if not type(msg) == bytes else msg.decode()

    def get_client(self):
        return self.client

    def close_socket(self):
        self.server.close()
