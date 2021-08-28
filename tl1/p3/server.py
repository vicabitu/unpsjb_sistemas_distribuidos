class Server:
    def __init__(self, adapter):
        self.adapter = adapter

    def inicializar(self):
        self.adapter.run()
