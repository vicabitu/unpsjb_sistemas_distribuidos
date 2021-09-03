from client import Client
from datetime import datetime
from timeit import default_timer
from datetime import timedelta

# Comentar y descomentar las importaciones de los stubs para cambiar el comportamiento del cliente

from p3a import ClientStub

# from p3b import ClientStub

CANT_BYTES = 2048


def get_extension_file(path):
    extension = path.split(".").pop()
    return extension


def leer_archivo(cliente, path):
    start = default_timer()
    can_open_file = cliente.abrir_archivo(path)

    if can_open_file:
        extension = get_extension_file(path)
        offset = 0
        today = datetime.now()
        file_name = f"new_file_{today.strftime('%d-%m-%Y_%H:%M:%S')}.{extension}"
        file = open(file_name, "wb")
        print("Descargando el archivo...")
        while True:
            bytes_leidos = cliente.leer_archivo(
                path,
                offset,
                CANT_BYTES,
            )
            offset += CANT_BYTES
            file.write(bytes_leidos)
            if len(bytes_leidos) == 0:
                break
        file.close()
        cliente.cerrar_archivo(path)
        end = default_timer()
        total_execution_time = timedelta(seconds=end - start)
        return [True, total_execution_time]
    else:
        return [False, None]


def listar_archivos(path, cliente):
    archivos = cliente.listar_archivos(path)
    if len(archivos) == 0:
        return False
    print(f"Se encontraron {len(archivos)} archivos:")
    for archivo in archivos:
        print(f"* {archivo}")
    return True


def show_path_menu():
    print("Ingrese la ruta del archivo:")
    path = input()
    return path


def main():
    stub = ClientStub("localhost", "50051")
    cliente = Client(stub)
    cliente.conectar()
    keep_working = True

    while keep_working:
        print("\n---------------------------------------------------")
        print("Ingrese una opción:")
        print("1 - Leer un archivo")
        print("2 - Listar archivos de un directorio")
        print("3 - salir")
        print("---------------------------------------------------")
        opcion = input()

        try:
            opcion = int(opcion)
            if opcion == 1:
                path = show_path_menu()
                print(f"Path ingresado: {path}")
                operation_result = leer_archivo(cliente, path)
                if operation_result[0]:
                    print("Descarga exitosa!")
                    print(f"Tiempo total de ejecucion: {operation_result[1]}")
                else:
                    print("No se encontró el archivo, vuelva a intentar")
            elif opcion == 2:
                path = show_path_menu()
                print(f"Path ingresado: {path}")
                operation_result = listar_archivos(path, cliente)
                if not operation_result:
                    print(f"No se encontraron archivos en el directorio {path}")
            elif opcion == 3:
                cliente.desconectar()
                break
            else:
                print("Opción no encontrada")
        except ValueError:
            print("Opción no encontrada")
        except KeyboardInterrupt:
            cliente.desconectar()
            break


if __name__ == "__main__":
    main()