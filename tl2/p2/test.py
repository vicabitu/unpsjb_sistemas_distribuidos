import sys
from client import Client


def main():
    try:
        server_name = sys.argv[1]
        client = Client(server_name)
        client.sync_with_server()
    except IndexError:
        print("Debe ingresar la ip o nombre del servidor NTP")


if __name__ == "__main__":
    main()
