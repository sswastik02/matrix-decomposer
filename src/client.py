import socket
import os
import numpy as np

from lib.network.client import Client
from lib.network.matrix import send_matrix
from constants.network import MSG_LEN
from constants.servers import CENTRAL_SERVER


def interface(s: socket.socket) -> None:
    matrix = np.array([[0, 1], [1, 2]])
    send_matrix(s, matrix)
    print(s.recv(MSG_LEN))
    s.close()


def main():
    host = os.getenv("HOST") or CENTRAL_SERVER.host
    port = os.getenv("PORT") or CENTRAL_SERVER.port
    port = int(port)
    client = Client(host, port)
    client.set_interface(interface)
    client.connect()


if __name__ == "__main__":
    main()
