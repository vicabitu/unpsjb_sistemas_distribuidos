import ntplib
from datetime import datetime


class Client:
    """Clase que representa al cliente de NTP"""

    FORMAT_DATE = "%Y-%m-%d %H:%M:%S%f"

    def __init__(self, server_name):
        self.server_name = server_name

    def convert_time_stamp_to_string_date(self, time_stamp):
        """Metodo que e encarga de convertir un timestamp
        de UNIX a un dormato de fecha legible por el usuario"""
        return datetime.fromtimestamp(time_stamp).strftime(Client.FORMAT_DATE)

    def display_information(self, response):
        """Metodo que se encarga de mostrar la informacion en pantalla al usuario"""
        print(f"* Precision: {response.precision}")
        print(f"* Root delay: {response.root_delay}")
        print(
            f"* T1 - Partida de solicitud: {self.convert_time_stamp_to_string_date(response.orig_timestamp)}"
        )
        print(
            f"* T2 - Hora del servidor: {self.convert_time_stamp_to_string_date(response.recv_timestamp)}"
        )
        print(
            f"* T3 - Respuesta del servidor: {self.convert_time_stamp_to_string_date(response.tx_timestamp)}"
        )
        print(
            f"* T4 - Arribo de respuesta del servidor: {self.convert_time_stamp_to_string_date(response.dest_timestamp)}"
        )
        print(f"* Tiempo de ida y vuelta: {response.delay}")
        print(f"* Local clock offset: {response.offset}")
        print(
            f"* Timestamp de referencia: {self.convert_time_stamp_to_string_date(response.ref_timestamp)}"
        )
        print(
            "---------------------------------------------------------------------------"
        )

    def sync_with_server(self):
        """Metodo que se encarga de generar la conexion con el servidor y hacer las peticiones NTP"""
        client = ntplib.NTPClient()
        print(f"Servidor: {self.server_name}")
        print(
            "---------------------------------------------------------------------------\n"
        )
        for i in range(1, 9):
            print(f"> Consulta: {i}\n")
            response = client.request(self.server_name, version=3)
            self.display_information(response)
