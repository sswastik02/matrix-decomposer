# Server

The Server is a class in [`lib/network/server.py`](../src/lib/network/server.py)
It deals with the server side of socket connection

### `Server.__init__(self, host, port)`
Listens on on `host`:`port`

* `host` : host for the server to listen on
* `port` : port on the host for the server to listen on

### `Server.set_client_handler(self, client_handler)`
Sets a valid client_handler for the server object

* `client_handler`: Callable that will be set and called in the `listener`

### `Server.listener(self)`
Infinite loop that accepts new connections and runs the `client_handler` on a new thread

### `Server.start(self)`
Binds to the given `host` and `port` while instantiating the server object and runs the `listener`

