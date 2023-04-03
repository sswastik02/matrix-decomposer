# Matrix


## Network Operations


### `send_matrix(socket, matrix)`
sends a matrix across a socket after encoding it

* `matrix`: The numpy array to be sent
* `socket`: The socket over which `matrix` will be sent

Encoding Procedure: 
1. Convert `matrix` to a bytes object using `pickle`
2. Prepend the length of matrix at the start in `little-endian`
3. Send the resultant message

### `recv_matrix(socket) -> numpy.array`
recieves a matrix across a socket after decoding it

* `socket`: The socket over which the matrix will be recived

Returns: `matrix` that was passed over socket

Decoding Procedure:
1. Recieve first 4 bytes of the message sent for the size of the encoded matrix
2. Compute the size from the recieved bytes and recieve only that many bytes over the `socket`

> __NOTE__: The maximum size of matrix is 2^16 due to the 4 bytes used for length