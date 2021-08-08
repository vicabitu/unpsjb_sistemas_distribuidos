class Server:

    def __init__(self, adapter=None):
        self.adapter = adapter

    def config(self):
        self.adapter.config()
    
    def start(self):
        self.adapter.start()

    def accept_connection(self):
        self.adapter.accept_connection()
    
    def close_connection(self):
        self.adapter.close_connection()

    def get_client(self):
        return self.adapter.get_client()

    def send(self, message):
        self.adapter.send(message)

    def receive(self):
        return self.adapter.receive()
