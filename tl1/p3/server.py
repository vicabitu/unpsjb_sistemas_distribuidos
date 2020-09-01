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

# use the generated function `add_FSServicer_to_server`
# to add the defined class to the server
file_system_pb2_grpc.add_FSServicer_to_server(
        FSServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
