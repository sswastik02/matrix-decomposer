import socket
import typing
import sys

from ..utils.logger import log


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

    def set_interface(self, interface: typing.Callable[[socket.socket], None]) -> None:
        "Sets an interface for the client"
        self.interface = interface

    def run_interface(self) -> None:
        "Runs the interface"
        self.interface(self.s)

    def connect(self, run_interface: bool = True) -> None:
        "Connects to the pre-specified host and port"
        try:
            self.s.connect((self.host, self.port))
        except ConnectionRefusedError:
            log.fatal(
                f'{self.host}:{self.port} is not reachable, make sure it is running')
            sys.exit(1)
        if run_interface:
            self.interface(self.s)
