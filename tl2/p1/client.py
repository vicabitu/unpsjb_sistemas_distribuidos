# saved as greeting-client.py
import Pyro4
import time
import threading
from datetime import datetime, timedelta


class ClockThread(threading.Thread):
    def __init__(self, remote_object, drift):
        self.time_server = remote_object
        self.drift = drift

    def convert_string_to_object_datetime(self, string_time):
        format = "%Y%m%d %H:%M:%S:%f"
        object_time = datetime.strptime(string_time, format)
        return object_time

    def run(self):

        smaller_half_round_trip_time = 1
        for i in range(5):
            # Uso de la deriva
            time.sleep(self.drift)
            beginning = time.time()

            string_server_time = self.time_server.get_time()

            end = time.time()

            round_trip_time = end - beginning

            server_time = self.convert_string_to_object_datetime(string_server_time)

            print(f"Tiempo total de ida y vuelta [C(T4) - C(T1)]: {round_trip_time}")

            half_round_trip_time = round_trip_time / 2

            if half_round_trip_time < smaller_half_round_trip_time:
                smaller_half_round_trip_time = half_round_trip_time

            print(f"> Tiempo total de ida [C(T4) - C(T1)] / 2: {half_round_trip_time}")

            print(f"Hora del servidor (T3): {string_server_time}")

            exact_hour = server_time + timedelta(seconds=half_round_trip_time)

            print(f"Hora exacta T3 + [C(T4) - C(T1)] / 2: {exact_hour}")
            print("---------------------------------------------------------------\n")
        print(f"Menor tiempor de ida: {smaller_half_round_trip_time}")
        return smaller_half_round_trip_time


def main():
    print("Main")
    time_server = Pyro4.Proxy(
        "PYRONAME:my.home"
    )  # use name server object lookup uri shortcut
    drift = 1
    clock = ClockThread(time_server, drift)
    smaller_half_round_trip_time = clock.run()

    print(f"Hora a fijar:")


if __name__ == "__main__":
    main()
