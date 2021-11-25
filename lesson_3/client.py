import sys
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEPORT


class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port

    def create_message(self):
        pass

    def send_request(self):
        pass

    def get_response(self):
        pass

    def get_message(self):
        pass

    def run(self):
        pass


def parse_command_line() -> tuple:
    pass


if __name__ == '__main__':
    address, port = parse_command_line()
    client = Client(address, port)
    client.run()
