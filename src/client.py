import socket
import numpy as np

from lib.network.client import Client
from lib.network.matrix import send_matrix, recv_matrix
from constants.network import MSG_LEN
from lib.utils.logger import log


def interface(s: socket.socket) -> None:
    n = int(input("Enter the value of n for n*n matrix: "))
    matrix = np.zeros((n,n))
    for i in range(n):
        row = input(f"Row {i+1}: ")
        elements = row.split()
        for j in range(n):
            matrix[i][j] = float(elements[j])
            
    send_matrix(s, matrix)
    upper = recv_matrix(s)
    lower = recv_matrix(s)
    print(f"Upper : {upper}")
    print(f"Lower : {lower}")
    print(f'Product :  {np.matmul(lower, upper)}')
    print(f'Actual : {matrix}')
    s.close()


def main():
    client = Client(name='central-server')
    client.set_interface(interface)
    client.connect()


if __name__ == "__main__":
    main()
    

