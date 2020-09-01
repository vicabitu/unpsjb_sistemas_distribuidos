import grpc
from concurrent import futures
import time

# import de las clases generadas
import file_system_pb2
import file_system_pb2_grpc

import file_system

class FSServicer(file_system_pb2_grpc.FSServicer):

    opened_files = {}

    def ListFiles(self, request, context):
        response = file_system_pb2.PathFiles()
        try:
            for file in file_system.list_files(request.value):
                response.values.append(file)            
        except Exception as e:
            print('ERRR En server list files ', e)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# agregar al servidor la clase definida mediante la
# funcion add_FSServicer_to_server
file_system_pb2_grpc.add_FSServicer_to_server(
        FSServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# dado que server.start() es no bloqueante,
# se agrega un sleep-loop para mantenerlo vivo
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
