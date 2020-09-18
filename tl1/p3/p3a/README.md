Pasos para generar las clases necesarias de gRPC.

0 - contar con grpcio y grpcio-tools
        pip install grpcio
        pip install grpcio-tools

1 - Define functions

2 - Define protocol buffer specification

3 - ejecutar
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_system.proto

    Notese que al final del comando figura el archivo de protocol buffer (file_system.proto) para la generación de las clases necesarias.

4 - Crear el servidor

5 - Crear un cliente



Konstantinoff Pedro 18/08/2020.