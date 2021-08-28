import socket
import threading
import sys
import pickle
import time


class FSStub(threading.Thread):
    def __init__(self, canal, file_system_adapter):
        threading.Thread.__init__(self)
        self._channel = canal
        self._adapter = file_system_adapter

    def run(self):
        time.sleep(15)
        data = self._channel.recv(4096)
        if not data:
            # TO DO: ver si es lo mejor el exit
            sys.exit()

        payload = pickle.loads(data)
        comando = payload.get("operacion", -1)
        if comando == 1:
            path = payload.get("path")
            path_files = self._adapter.list_files(path)
            response = {"paths": path_files}
            response_serialized = pickle.dumps(response)
            self._channel.sendall(response_serialized)
        elif comando == 2:
            path = payload.get("path")
            open = self._adapter.open_file(path)
            response = {"open": open}
            response_serialized = pickle.dumps(response)
            self._channel.sendall(response_serialized)
        elif comando == 3:
            path = payload.get("path")
            data_file = self._adapter.read_file(path)
            response = {"data_file": data_file}
            response_serialized = pickle.dumps(response)
            self._channel.sendall(response_serialized)
        elif comando == 4:
            path = payload.get("path")
            close = self._adapter.close_file(path)
            response = {"close": close}
            response_serialized = pickle.dumps(response)
            self._channel.sendall(response_serialized)


class Stub:
    def __init__(self, adapter, port="8090"):
        self._port = int(port)
        self._adapter = adapter
        self.server = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", self._port))

    def run(self):
        self._setup()
        self.server.listen()
        try:
            print("Aceptando una conexion")
            while True:
                connection, client_address = self.server.accept()
                print(
                    "Connected to: " + client_address[0] + ":" + str(client_address[1])
                )
                thread = FSStub(connection, self._adapter)
                thread.start()

        except KeyboardInterrupt:
            print("Exit the server")
            self.server.close()
