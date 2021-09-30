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
        format = "%Y-%m-%d %H:%M:%S:%f"
        object_time = datetime.strptime(string_time, format)
        return object_time

    def get_smallest_round_trip_time(self, times):
        result = times[0]
        smaller = times[0].get("half_round_trip_time")
        for t in times:
            if t.get("half_round_trip_time") < smaller:
                smaller = t.get("half_round_trip_time")
                result = t
        return result

    def run(self):

        times = []

        for i in range(5):
            # Uso de la deriva
            beginning = time.time()

            string_server_time = self.time_server.get_time()

            end = time.time()

            round_trip_time = end - beginning

            server_time = self.convert_string_to_object_datetime(string_server_time)

            print(f"Tiempo total de ida y vuelta [C(T4) - C(T1)]: {round_trip_time}")

            half_round_trip_time = round_trip_time / 2

            times.append(
                {
                    "half_round_trip_time": half_round_trip_time,
                    "server_time": server_time,
                }
            )

            print(f"> Tiempo total de ida [C(T4) - C(T1)] / 2: {half_round_trip_time}")
            print(f"Hora del servidor (T3): {string_server_time}")
            print("---------------------------------------------------------------\n")

        shorter_half_round_trip_time = self.get_smallest_round_trip_time(times)
        print(f"El tiempo mas corto: {shorter_half_round_trip_time}")
        exact_hour = shorter_half_round_trip_time.get("server_time") + timedelta(
            seconds=shorter_half_round_trip_time.get("half_round_trip_time")
        )
        print(f"Hora exacta: {exact_hour}")
        # time.sleep(self.drift)
        return exact_hour


def main():
    time_server = Pyro4.Proxy(
        "PYRONAME:my.home"
    )  # use name server object lookup uri shortcut
    drift = 1
    # aca tengo que instanciar una hora inicial hardcodeada, futura o pasada
    clock = ClockThread(time_server, drift)
    test_date = datetime(2021, 9, 25)
    print("test_date", test_date)
    exact_hour = clock.run()


if __name__ == "__main__":
    main()
