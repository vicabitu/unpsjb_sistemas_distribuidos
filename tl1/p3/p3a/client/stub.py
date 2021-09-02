import grpc

from file_system_pb2 import Path, Offset, CantBytes, ReadFileParameters
from file_system_pb2_grpc import FSStub


class Stub:
    def __init__(self, host="0.0.0.0", port="50051"):
        self._appliance = ":".join([host, port])
        self._channel = None
        self._stub = None

    def connect(self):
        """ Returns a gRPC open channel """
        try:
            self._channel = grpc.insecure_channel(self._appliance)
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
            path = Path(value=path)
            response = self._stub.ListFiles(path)
            return response.values
        return None

    def open_file(self, path):
        path = Path(value=path)
        response = self._stub.OpenFile(path)
        return response.value

    def read_file(self, path, offset, cant_bytes):
        path = Path(value=path)
        offset = Offset(value=offset)
        cant_bytes = CantBytes(value=cant_bytes)
        read_file_parameters = ReadFileParameters(
            path=path, offset=offset, cant_bytes=cant_bytes
        )
        response = self._stub.ReadFile(read_file_parameters)
        return response.value

    def close_file(self, path):
        path = Path(value=path)
        response = self._stub.CloseFile(path)
        return response.value
