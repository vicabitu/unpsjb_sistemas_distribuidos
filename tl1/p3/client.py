import grpc

# import the generated classes
import file_system_pb2
import file_system_pb2_grpc

# abrir un canal gRPC
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = file_system_pb2_grpc.FSStub(channel)

directorio = '.'
path = file_system_pb2.Path(value=directorio)
response = stub.ListFiles(path)
print(response.values)
