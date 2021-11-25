import sys
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEPORT


class MessageServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def get_message(self, sock):
        data = sock.recv(1280)
        pass

    def create_response(self):
        pass

    def send_response(self):
        pass

    def run(self):
        client, addr = self.sock.accept()
        message = self.get_message(client)
        pass


def parse_command_line() -> tuple:
    # TODO: реализовать проверки

    address = ''
    port = 7777
    command_args = sys.argv
    if len(command_args) == 4:

        try:
            port = int(command_args[command_args.index('-p') + 1])
        except ValueError:
            return 'Порт должен быть целым числом'

        try:
            address = command_args[command_args.index('-a') + 1]
        except:
            return

    print(1)
    return address, port


def main():
    # TODO: реализовать все проверки здесь
    address, port = parse_command_line()
    server = MessageServer(address, port)
    # server.run()


if __name__ == '__main__':
    main()
