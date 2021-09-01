from concurrent.futures.thread import ThreadPoolExecutor
import socket
import pickle


def process_request(canal, file_system_adapter):
    print("> 1 process_request")
    while True:
        data = canal.recv(4096)
        if not data:
            break

        payload = pickle.loads(data)
        comando = payload.get("operacion", -1)
        if comando == 1:
            path = payload.get("path")
            path_files = file_system_adapter.list_files(path)
            response = {"paths": path_files}
            response_serialized = pickle.dumps(response)
            canal.sendall(response_serialized)
        elif comando == 2:
            path = payload.get("path")
            open = file_system_adapter.open_file(path)
            response = {"open": open}
            response_serialized = pickle.dumps(response)
            canal.sendall(response_serialized)
        elif comando == 3:
            path = payload.get("path")
            offset = payload.get("offset")
            cant_bytes = payload.get("cant_bytes")
            data_file = file_system_adapter.read_file(path, offset, cant_bytes)
            response = {"data_file": data_file}
            response_serialized = pickle.dumps(response)
            canal.sendall(response_serialized)
        elif comando == 4:
            path = payload.get("path")
            close = file_system_adapter.close_file(path)
            response = {"close": close}
            response_serialized = pickle.dumps(response)
            canal.sendall(response_serialized)


class Stub:
    def __init__(self, adapter, port="8090"):
        self._port = int(port)
        self._adapter = adapter
        self.server = None
        self._stub = None
        self._executor = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", self._port))
        self._executor = ThreadPoolExecutor(max_workers=3)

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                print("Aceptando una conexion")
                connection, client_address = self.server.accept()
                print(f"Connected to: {client_address[0]}:{str(client_address[1])}\n")
                self._executor.submit(process_request, connection, self._adapter)
        except KeyboardInterrupt:
            print("\nExit the server")
            self.server.close()
