import socket
import typing

from ..utils.signals import *


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def set_interface(self, interface: typing.Callable[[socket.socket], None]) -> None:
        "Sets an interface for the client"
        self.interface = interface

    def connect(self) -> None:
        "Connects to the pre-specified host and port"
        self.s.connect((self.host, self.port))
        self.interface(self.s)
