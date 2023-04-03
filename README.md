# Matrix Decomposer Service

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>

**_A Client-Server model service built using python socket library which decomposes a given matrix_**

# Setup

## Dependencies

```sh
python3 -m venv venv # if you have not created a virtual environment yet
source venv/bin/activate
pip install -r requirements.txt
```

> **NOTE:** Make sure python is installed on your system (prefereably the one indicated in `.python-version`)

# Run

## Central Server

```sh
python3 src/server.py
```

## Client

```sh
python3 src/client.py

```

# Docmentation

## Architecture

<img src="./docs/img/architecture.png" width="1024px"/>

| Service        | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| Central Server | Interacts with client and manages the worker servers      |
| Client         | Interact with the Central Server                          |
| L Worker       | Computes the L of a Matrix Decomposition Problem `A = LU` |
| U Worker       | Computes the U of a Matrix Decomposition Problem `A = LU` |

## Code Documentation

The documentation for specific code can be found [here](./docs/index.md)

### Server

A python class providing logic for the server that uses python `sockets` and handles every client in a seperate thread. For further [info](./docs/Server.md)

### Client

A python class providing logic for the client that uses python `sockets` and connects to server. For further [info](./docs/Client.md)

# Contributors

| Name             | Github ID                                     |
| ---------------- | --------------------------------------------- |
| `Amool Kuldiya`  | [amool-kk](https://github.com/Amool-kk)       |
| `Kaushal Baid`   | [kaushal168](https://github.com/kaushal168)   |
| `Niraj Kumar`    | [nirajraj-13](https://github.com/nirajraj-13) |
| `Shruti Singh`   | [Shru-Singh](https://github.com/Shru-Singh)   |
| `Swastik Sarkar` | [sswastik02](https://github.com/sswastik02)   |
