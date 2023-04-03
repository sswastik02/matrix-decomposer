import socket
import threading
import typing

from ..utils.logger import log
from ..utils.signals import *


class Server:
    def __init__(self, host: str, port: int) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port

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

    def start(self, n: int = 5) -> None:
        "Starting Server with a listener"
        try:
            self.s.bind((self.host, self.port))
        except OSError:
            log.fatal(f'{self.host}:{self.port} is already in use, use another port using environment variables')
            sys.exit(1)

        self.s.listen(n)
        log.info(f"Listening on {self.host}:{self.port}")
        self.listener()

