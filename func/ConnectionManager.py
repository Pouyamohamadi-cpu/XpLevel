import socket

class ConnectionManager:
    def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM):
        self.sock = socket.socket(family, type)

    def bind(self, address):
        self.sock.bind(address)

    def listen(self, backlog=5):
        self.sock.listen(backlog)

    def accept(self):
        return self.sock.accept()

    def connect(self, address):
        self.sock.connect(address)

    def send(self, data):
        self.sock.send(data)

    def recv(self, bufsize):
        return self.sock.recv(bufsize)

    def close(self):
        self.sock.close()
