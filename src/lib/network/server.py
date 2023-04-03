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
        self.client_handler = client_handler

    def listener(self) -> None:
        while True:
            cli, ip = self.s.accept()
            log.info(f'[*] New Connection : {ip}')
            client_thread = threading.Thread(
                target=self.client_handler, args=(cli, ip)
            )
            client_thread.start()

    def start(self, n: int = 5) -> None:
        self.s.bind((self.host, self.port))
        self.s.listen(n)
        log.info(f"Listening on {self.host}:{self.port}")
        self.listener()
