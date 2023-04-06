import os
import socket
import numpy as np
from numpy.typing import ArrayLike

from constants.servers import CENTRAL_SERVER, L_SERVER, U_SERVER
from lib.network.server import Server
from lib.network.client import Client
from lib.network.matrix import recv_matrix, send_matrix


def client_handler(cli: socket.socket, ip: any) -> None:
    with cli:
        matrix = recv_matrix(cli)
        n = len(matrix)
        decomposed_matrices: dict = {}

        def l_interface(s: socket.socket):
            send_matrix(s, matrix)
            lower_matrix = recv_matrix(s)
            decomposed_matrices["lower"] = lower_matrix

        def u_interface(s: socket.socket):
            send_matrix(s, matrix)
            upper_matrix = recv_matrix(s)
            decomposed_matrices["upper"] = upper_matrix

        l_client.set_interface(l_interface)
        u_client.set_interface(u_interface)
        l_client.run_interface()
        u_client.run_interface()
        cli.send(f'Decomposed {decomposed_matrices}'.encode())


def main():
    host = os.getenv("HOST") or CENTRAL_SERVER.host
    port = os.getenv("PORT") or CENTRAL_SERVER.port
    port = int(port)

    global l_client
    global u_client

    server = Server(host, port)
    l_client = Client(L_SERVER.host, L_SERVER.port)
    u_client = Client(U_SERVER.host, U_SERVER.port)

    l_client.connect(run_interface=False)
    u_client.connect(run_interface=False)
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
