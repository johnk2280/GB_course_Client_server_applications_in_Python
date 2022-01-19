import sys
import json
from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEPORT
import logging

import lesson_6.log.server_log_config

server_logger = logging.getLogger('server')


class MessageServer:
    def __init__(self, address, port):
        self.address = address
        self.port = port

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.address, self.port))
        self.sock.listen()

    def get_data(self, message: bytes) -> dict:
        server_logger.debug('Получение данных из сообщения')
        return json.loads(message.decode('utf-8'))

    def create_response(self, data: dict) -> bytes:
        server_logger.debug('Формирование ответа')
        if list(data.keys()) == ['action', 'time', 'type', 'user'] and data['action'] == 'presence':
            return json.dumps({'response': 200}).encode('utf-8')

        return json.dumps({'response': 400}).encode('utf-8')

    def run(self) -> None:
        while True:
            server_logger.debug('Запуск сервера')
            client, address = self.sock.accept()
            server_logger.debug('Сервер запущен')
            message = client.recv(1280)
            server_logger.debug(f'Получено сообщение - {message}')
            data = self.get_data(message)
            response = self.create_response(data)
            server_logger.debug(f'Сформирован ответ - {response}')
            client.send(response)
            server_logger.debug('Ответ отправлен')
            client.close()
            server_logger.debug('Соединение с клиентом закрыто')


def parse_command_line() -> tuple:
    address = '127.0.0.1'
    port = 7777
    command_args = sys.argv
    if '-p' in command_args:
        try:
            port = int(command_args[command_args.index('-p') + 1])
            if port < 1024 or port > 65535:
                raise ValueError
        except IndexError:
            server_logger.debug('Не указан порт')
            sys.exit(-1)
        except ValueError:
            server_logger.debug('Указан неверный порт')
            sys.exit(-1)

    if '-a' in command_args:
        try:
            address = command_args[command_args.index('-a') + 1]
        except IndexError:
            server_logger.debug('Не указан адрес')
            sys.exit(1)

    return address, port


def main() -> None:
    address, port = parse_command_line()
    server = MessageServer(address, port)
    server.run()


if __name__ == '__main__':
    main()