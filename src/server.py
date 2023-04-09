import os
import socket
import threading
from typing import List

from constants.servers import CENTRAL_SERVER
from lib.network.server import Server
from lib.network.client import Client
from lib.network.matrix import recv_matrix, send_matrix


def client_handler(cli: socket.socket, ip: any) -> None:
    with cli:
        matrix = recv_matrix(cli)
        decomposed_matrices: dict = {}
        lock = threading.Lock()

        def l_interface(s: socket.socket):
            send_matrix(s, matrix)
            lower_matrix = recv_matrix(s)
            with lock:
                decomposed_matrices["lower"] = lower_matrix

        def u_interface(s: socket.socket):
            send_matrix(s, matrix)
            upper_matrix = recv_matrix(s)
            with lock:
                decomposed_matrices["upper"] = upper_matrix

        l_client.set_interface(l_interface)
        u_client.set_interface(u_interface)

        jobs:List[threading.Thread] = []
        jobs.append(threading.Thread(target=l_client.run_interface))
        jobs.append(threading.Thread(target=u_client.run_interface))

        for job in jobs:
            job.start()
        for job in jobs:
            job.join()
        
        l_client.run_interface()
        u_client.run_interface()
        send_matrix(cli, decomposed_matrices["upper"])
        send_matrix(cli, decomposed_matrices["lower"])


def main():
    host = os.getenv("HOST") or CENTRAL_SERVER.host
    port = os.getenv("PORT") or CENTRAL_SERVER.port
    port = int(port)

    global l_client
    global u_client

    server = Server(host, port, server_name="central-server")
    l_client = Client(name='l-decomposer')
    u_client = Client(name='u-decomposer')

    l_client.connect(run_interface=False)
    u_client.connect(run_interface=False)
    server.set_client_handler(client_handler)
    server.start()


if __name__ == "__main__":
    main()
