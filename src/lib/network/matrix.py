import socket
import struct
import pickle
from numpy.typing import ArrayLike


def send_matrix(s: socket.socket, matrix: ArrayLike) -> None:
    "Sends matrix over socket"
    encodedMatrix = pickle.dumps(matrix)
    msg = struct.pack('>I', len(encodedMatrix)) + encodedMatrix
    s.sendall(msg)


def recv_matrix(s: socket.socket) -> ArrayLike:
    "Recieves matrix over a socket"
    raw_msg_len = s.recv(4)
    msg_len = struct.unpack('>I', raw_msg_len)[0]
    matrix = s.recv(msg_len)
    matrix = pickle.loads(matrix)
    return matrix
