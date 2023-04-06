import socket

from constants.servers import U_SERVER
from lib.network.server import Server
from lib.network.matrix import recv_matrix, send_matrix
from lib.math.matrix import uDecomposition
from lib.utils.logger import log


def client_handler(cli: socket.socket, ip: any) -> None:
    with cli:
        while True:
            matrix = recv_matrix(cli)
            u_matrix = uDecomposition(matrix)
            log.debug(f'Recieved from {ip} :\n {matrix}')
            log.debug(f'Decomposed :\n {u_matrix}')
            send_matrix(cli, u_matrix)


def main():
    host = U_SERVER.host
    port = U_SERVER.port
    port = int(port)

    server = Server(host, port)
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
