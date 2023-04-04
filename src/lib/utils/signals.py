import sys
import socket

from .logger import log


def sigint_handler(sig, frame, s:socket.socket):
    log.critical("Exiting SIGINT recieved")
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    sys.exit(0)
