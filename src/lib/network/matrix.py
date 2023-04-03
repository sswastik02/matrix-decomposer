import socket
import numpy as np
import struct
import pickle


def send_matrix(s: socket.socket, matrix: np.array) -> None:
    "Sends matrix over socket"
    encodedMatrix = pickle.dumps(matrix)
    msg = struct.pack('>I', len(encodedMatrix)) + encodedMatrix
    s.sendall(msg)


def recv_matrix(s: socket.socket) -> np.array:
    "Recieves matrix over a socket"
    raw_msg_len = s.recv(4)
    msg_len = struct.unpack('>I', raw_msg_len)[0]
    matrix = s.recv(msg_len)
    matrix = pickle.loads(matrix)
    return matrix
