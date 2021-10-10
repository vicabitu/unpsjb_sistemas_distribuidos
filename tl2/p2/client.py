import sys
import ntplib
from datetime import datetime


def convert_time_stamp_to_date_string(time_stamp):
    return datetime.fromtimestamp(time_stamp).strftime("%Y-%m-%d %H:%M:%S%f")


def main():
    server_name = sys.argv[1]
    client = ntplib.NTPClient()
    print(f"Servidor: {server_name}")
    print(
        "---------------------------------------------------------------------------\n"
    )
    for i in range(1, 9):
        print(f"Consulta: {i}\n")
        response = client.request(server_name, version=3)
        print(f"Precision: {response.precision}")
        print(f"Root delay: {response.root_delay}")
        print(
            f"T1 - Partida de solicitud: {convert_time_stamp_to_date_string(response.orig_timestamp)}"
        )
        print(
            f"T2 - Hora del servidor: {convert_time_stamp_to_date_string(response.recv_timestamp)}"
        )
        print(
            f"T3 - Respuesta del servidor: {convert_time_stamp_to_date_string(response.tx_timestamp)}"
        )
        print(
            f"T4 - Arribo de respuesta del servidor: {convert_time_stamp_to_date_string(response.dest_timestamp)}"
        )
        print(f"Tiempo de ida y vuelta: {response.delay}")
        print(f"Local clock offset: {response.offset}")
        print(
            f"Timestamp de referencia: {convert_time_stamp_to_date_string(response.ref_timestamp)}"
        )
        print(
            "---------------------------------------------------------------------------"
        )


if __name__ == "__main__":
    main()
