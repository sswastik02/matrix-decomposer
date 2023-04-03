# Client

The Client is a class in [`lib/network/client.py`](../src/lib/network/client.py)
It deals with the client side of socket connection

### `Client.__init__(self, host, port)`
Connects to a socket service running on `host`:`port`

* `host` : host for the client to connect to
* `port` : port on the host for the client to connect to 

### `Client.set_interface(self, interface)`
Sets a valid interface for the client object

* `interface`: Callable that will be set and called during `connect` operation

### `Client.connect(self)`
Connects to the given `host` and `port` while instantiating the client object and runs the `interface`

