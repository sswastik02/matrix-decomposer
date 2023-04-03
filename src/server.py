from lib.network.server import Server
import os
import socket
from constants.servers import CENTRAL_SERVER


def client_handler(cli: socket.socket, ip: any) -> None:
    cli.send(f"Connected Successfuly your ip is {ip}".encode())


def main():
    host = os.getenv("HOST") or CENTRAL_SERVER.host
    port = os.getenv("PORT") or CENTRAL_SERVER.port
    port = int(port)

    server = Server(host, port)
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
