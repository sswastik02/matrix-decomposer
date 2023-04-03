import os
import socket

from constants.servers import CENTRAL_SERVER
from lib.network.server import Server
from lib.network.matrix import recv_matrix


def client_handler(cli: socket.socket, ip: any) -> None:
    matrix = recv_matrix(cli)
    cli.send(f"Hello {ip} recieved {matrix}".encode())


def main():
    host = os.getenv("HOST") or CENTRAL_SERVER.host
    port = os.getenv("PORT") or CENTRAL_SERVER.port
    port = int(port)

    server = Server(host, port)
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
