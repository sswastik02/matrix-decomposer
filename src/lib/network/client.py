import socket
import typing
import sys

from ..utils.logger import log
from constants.servers import DNS
from constants.network import MSG_LEN


class Client:
    def __init__(self, name: str = None) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
        if ':' in name:
            self.host,self.port = name.split(':')
            self.port = int(self.port)
        else:
            self.resolve_dns()

    def set_interface(self, interface: typing.Callable[[socket.socket], None]) -> None:
        "Sets an interface for the client"
        self.interface = interface

    def run_interface(self) -> None:
        "Runs the interface"
        self.interface(self.s)

    def resolve_dns(self) -> None:
        with self.s:
            try:
                self.s.connect((DNS.host, DNS.port))
            except ConnectionRefusedError:
                log.fatal(
                    f'{DNS.host}:{DNS.port} is not reachable, make sure DNS is running')
                sys.exit(1)
            self.s.send(self.name.encode())
            ip = self.s.recv(MSG_LEN).decode()
            host, port = ip.split(':')
            port = int(port)
            self.host, self.port = host, port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Workaround to reuse socket

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
