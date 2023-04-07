import os
import socket

from constants.servers import L_SERVER
from lib.network.server import Server
from lib.network.matrix import recv_matrix, send_matrix
from lib.math.matrix import lDecomposition
from lib.utils.logger import log


def client_handler(cli: socket.socket, ip: any) -> None:
    with cli:
        while True:
            matrix = recv_matrix(cli)
            l_matrix = lDecomposition(matrix)
            log.debug(f'Recieved from {ip} :\n {matrix}')
            log.debug(f'Decomposed :\n {l_matrix}')
            send_matrix(cli, l_matrix)


def main():
    host = os.getenv("HOST") or L_SERVER.host
    port = os.getenv("PORT") or L_SERVER.port
    port = int(port)

    server = Server(host, port, server_name="l-decomposer")
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
