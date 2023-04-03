import socket
import os
import numpy as np
import pickle

from lib.network.client import Client
from constants.network import MSG_LEN
from constants.servers import CENTRAL_SERVER


def interface(s: socket.socket) -> None:
    x = s.recv(MSG_LEN)
    print(x)
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
