import socket
import pickle


class FSStub:
    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        payload = {"path": path, "operacion": 1}
        payload_serialized = pickle.dumps(payload)
        self._channel.sendall(payload_serialized)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("paths")

    def openFile(self, path):
        payload = {"path": path, "operacion": 2}
        payload_serialized = pickle.dumps(payload)
        self._channel.sendall(payload_serialized)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("open")

    def readFile(self, path):
        payload = {"path": path, "operacion": 3}
        payload_serialized = pickle.dumps(payload)
        self._channel.sendall(payload_serialized)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("data_file")

    def closeFile(self, path):
        payload = {"path": path, "operacion": 4}
        payload_serialized = pickle.dumps(payload)
        self._channel.sendall(payload_serialized)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("close")


class Stub:
    def __init__(self, host="0.0.0.0", port="8090"):
        self._appliance = (host, int(port))
        self._channel = None
        self._stub = None

    def connect(self):
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print("Error when openning channel {}".format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, path):
        if self.is_connected():
            return self._stub.ListFiles(path)
        return None

    def open_file(self, path):
        return self._stub.openFile(path)

    def read_file(self, path):
        return self._stub.readFile(path)

    def close_file(self, path):
        return self._stub.closeFile(path)
