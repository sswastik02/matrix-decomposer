import socket
from threading import Lock

from constants.servers import DNS
from constants.network import MSG_LEN
from lib.network.server import Server
from lib.utils.logger import log

lock = Lock()
dns_map = {}


def client_handler(cli: socket.socket, ip: any) -> None:
    global dns_map
    with cli:
        req = cli.recv(MSG_LEN).decode()
        if '@' in req:
            # Update DNS record
            name, ip = req.split('@')
            with lock:
                dns_map[name] = ip
            log.debug(f'Updated Record for {name}: {ip}')
            log.debug(f'Final DNS State: {dns_map}')
        else:
            try:
                name = req
                ip = dns_map[name]
                log.debug(f'Resolving {name} : {ip}')
                cli.send(ip.encode())
            except:
                cli.send(b'DNS Record Not found')


def main():
    host = DNS.host
    port = DNS.port
    port = int(port)

    server = Server(host, port, server_name="DNS")
    server.set_client_handler(client_handler)
    server.start(register_dns=False)


if __name__ == "__main__":
    main()
