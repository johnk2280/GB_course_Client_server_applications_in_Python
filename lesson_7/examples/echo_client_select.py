from socket import socket, AF_INET, SOCK_STREAM
from select import select
import sys


ADDRESS = ('localhost', 10000)


def echo_client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'exit':
                break

            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            print(f'Ответ: {data}')


if __name__ == '__main__':
    echo_client()
