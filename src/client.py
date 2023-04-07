import socket
import numpy as np

from lib.network.client import Client
from lib.network.matrix import send_matrix
from constants.network import MSG_LEN


def interface(s: socket.socket) -> None:
    with s:
        matrix = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])
        send_matrix(s, matrix)
        print(s.recv(MSG_LEN))


def main():
    client = Client(name='central-server')
    client.set_interface(interface)
    client.connect()


if __name__ == "__main__":
    main()
