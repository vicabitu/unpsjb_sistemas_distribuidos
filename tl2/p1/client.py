import Pyro4
import time
import threading
from datetime import datetime, timedelta
from timeit import default_timer


class ClockThread(threading.Thread):
    def __init__(self, remote_object, client_hour):
        self.time_server = remote_object
        self.client_hour = client_hour

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

    def calculate_time_difference(self, server_hour):
        difference = server_hour - self.client_hour
        return difference.total_seconds()

    def process_difference(self, difference):
        if difference >= 60:
            return -1  # me duermo 0
        elif difference >= 30:
            return -0.8  # me duero 0.2
        elif difference >= 1:
            return -0.6  # me duermo 0.4
        elif difference > -1 and difference < 1:
            return 0  # me duermo 1
        # A partir de aca me tengo que retrasar, me duermo mas (Estoy adelantado)
        elif difference <= -60:
            return 12
        elif difference <= -30:
            return 7
        elif difference <= -1:
            return 0.6
        else:
            return 10

    def process_drift(self, drift):
        time.sleep(1 + drift)

    def cristian_algorithm(self):

        times = []

        for i in range(5):
            beginning = time.time()

            string_server_time = self.time_server.get_time()

            end = time.time()

            round_trip_time = end - beginning

            server_time = self.convert_string_to_object_datetime(string_server_time)

            # print(f"Tiempo total de ida y vuelta [C(T4) - C(T1)]: {round_trip_time}")

            half_round_trip_time = round_trip_time / 2

            times.append(
                {
                    "half_round_trip_time": half_round_trip_time,
                    "server_time": server_time,
                }
            )

            # print(f"> Tiempo total de ida [C(T4) - C(T1)] / 2: {half_round_trip_time}")
            # print(f"Hora del servidor (T3): {string_server_time}")
            # print("---------------------------------------------------------------\n")

        shorter_half_round_trip_time = self.get_smallest_round_trip_time(times)

        server_time = shorter_half_round_trip_time.get("server_time")
        shorter_half_round_trip_time = shorter_half_round_trip_time.get(
            "half_round_trip_time"
        )
        exact_hour = server_time + timedelta(seconds=shorter_half_round_trip_time)

        return exact_hour

    def run(self):

        quantity = 0

        # ayuda cuando el reloj esta lejos
        # El numero representa las veces que tengo que iterar para llamar a cristian otra vez
        while True:
            start = default_timer()
            if quantity == 0:
                server_hour = self.cristian_algorithm()
                difference = self.calculate_time_difference(server_hour)
                drift = self.process_difference(difference)
                d = abs(difference) // 2000
                quantity = d
            else:
                quantity -= 1
            self.process_drift(drift)
            self.client_hour += timedelta(seconds=1)
            end = default_timer()
            total_execution_time = timedelta(seconds=end - start)

            print(
                f"Hora del cliente: {self.client_hour} - Deriva: {drift} - Diferencia: {difference} - q: {quantity} - Tiempo de ejecucion: {total_execution_time}"
            )


def main():
    time_server = Pyro4.Proxy(
        "PYRONAME:my.home"
    )  # use name server object lookup uri shortcut
    # aca tengo que instanciar una hora inicial hardcodeada, futura o pasada
    # test_date = datetime(2021, 9, 25)
    # test_date = datetime(2021, 9, 30, 19, 50, 0)
    # test_date = datetime(2021, 10, 7, 19, 54, 0)
    test_date = datetime(2021, 10, 8, 15, 18, 0)
    clock = ClockThread(time_server, test_date)
    print(f"Hora del cliente {test_date}")
    clock.run()


if __name__ == "__main__":
    main()
