import sys
import json
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEPORT


class MessageServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def get_data(self, message: bytes) -> dict:
        return json.loads(message.decode('utf-8'))

    def get_status(self, param):
        pass

    def create_response(self, data: dict) -> bytes:
        if list(data.keys()) == ['action', 'time', 'type', 'user'] and data['action'] == 'presence':
            return json.dumps({'response': 200}).encode('utf-8')

        return json.dumps({'response': 400}).encode('utf-8')

    def run(self) -> None:
        while True:
            client, address = self.sock.accept()
            message = client.recv(1280)
            data = self.get_data(message)
            response = self.create_response(data)
            client.send(response)
            client.close()


def parse_command_line() -> tuple:
    address = ''
    port = 7777
    command_args = sys.argv
    if '-p' in command_args:
        try:
            port = int(command_args[command_args.index('-p') + 1])
            if port < 1024 or port > 65535:
                raise ValueError
        except IndexError:
            print('После параметра -\'p\' необходимо указать номер порта.')
            sys.exit(-1)
        except ValueError:
            print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            sys.exit(-1)

    if '-a' in command_args:
        try:
            address = command_args[command_args.index('-a') + 1]
        except IndexError:
            print('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
            sys.exit(1)

    return address, port


def main() -> None:
    address, port = parse_command_line()
    server = MessageServer(address, port)
    server.run()


if __name__ == '__main__':
    main()
