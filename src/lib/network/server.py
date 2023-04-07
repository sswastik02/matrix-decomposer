import socket
import threading
import typing
import sys

from ..utils.logger import log
from constants.servers import DNS


class Server:
    def __init__(self, host: str, port: int, server_name: str) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.server_name = server_name
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def set_client_handler(self, client_handler: typing.Callable[[socket.socket, any], None]) -> None:
        "Sets a client handler for the server object"
        self.client_handler = client_handler

    def listener(self) -> None:
        "Listens for new connections and starting in threads"
        while True:
            cli, ip = self.s.accept()
            log.info(f'[*] New Connection : {ip}')
            client_thread = threading.Thread(
                target=self.client_handler, args=(cli, ip)
            )
            client_thread.start()

    def register_dns(self) -> None:
        with self.s:
            try:
                self.s.connect((DNS.host, DNS.port))
            except ConnectionRefusedError:
                log.fatal(
                    f'{DNS.host}:{DNS.port} is not reachable, make sure DNS is running')
                sys.exit(1)
            self.s.send(f'{self.server_name}@{self.host}:{self.port}'.encode())
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Workaround to reuse socket

    def start(self, n: int = 5, register_dns: bool = True) -> None:
        "Starting Server with a listener"
        if register_dns:
            self.register_dns()
        try:
            self.s.bind((self.host, self.port))
        except OSError:
            log.fatal(
                f'{self.host}:{self.port} is already in use, use another port using environment variables')
            sys.exit(1)

        self.s.listen(n)
        log.info(f"Listening on {self.host}:{self.port}")
        try:
            self.listener()
        except KeyboardInterrupt:
            log.critical("Exiting SIGINT recieved")
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            sys.exit(0)
