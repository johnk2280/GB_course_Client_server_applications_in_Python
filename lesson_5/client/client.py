import logging
import sys
import json
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEPORT

import lesson_5.log.client_log_config

client_logger = logging.getLogger('client')


class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.address, self.port))

    def create_message(self) -> bytes:
        client_logger.debug('Создание сообщения для отправки')
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }
        return json.dumps(data).encode('utf-8')

    def send_request(self, message: bytes) -> None:
        client_logger.debug('Отправка сообщения')
        self.sock.send(message)

    def get_response(self, response: bytes) -> dict:
        return json.loads(response.decode('utf-8'))

    def run(self) -> None:
        client_logger.debug('Запуск клиента')
        self.send_request(self.create_message())
        client_logger.debug('Сообщение отправлено')
        response = self.get_response(self.sock.recv(1280))
        client_logger.debug(f'Получен ответ сервера - {response}')


def parse_command_line() -> tuple:
    command_args = sys.argv
    try:
        address = command_args[1]
        port = int(command_args[2])
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        address = '127.0.0.1'
        port = 7777
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(-1)

    return address, port


if __name__ == '__main__':
    address, port = parse_command_line()
    client = Client(address, port)
    client.run()
