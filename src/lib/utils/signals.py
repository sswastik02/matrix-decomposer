import signal
from .logger import log
import sys


def sigint_handler(sig, frame):
    log.critical("Exiting SIGINT recieved")
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)
