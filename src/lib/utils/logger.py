import logging
import sys


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    green = "\x1b[0;32m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    purple = "\x1b[0;35m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: purple + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
filehdlr = logging.FileHandler("/dev/null")
streamhdlr = logging.StreamHandler(sys.stdout)
streamhdlr.setFormatter(CustomFormatter())
log.addHandler(streamhdlr)
log.addHandler(filehdlr)
