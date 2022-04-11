import time
import select
from socket import socket, AF_INET, SOCK_STREAM


def new_listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    return sock


def main_loop():
    address = ('', 8888)
    clients = []
    sock = new_listen_socket(address)
    while True:
        try:
            connection, addr = sock.accept()
        except OSError:
            pass
        else:
            print(f"Получен запрос на соединение с {addr}")
            clients.append(connection)
        finally:
            writes = []
            try:
                reads, writes, errors = select.select([], clients, [], 0)
            except Exception:
                pass

            for sock_client in writes:
                time_str = time.ctime(time.time()) + "\n"
                try:
                    sock_client.send(time_str.encode('utf-8'))
                except:
                    clients.remove(sock_client)


print('Эхо-сервер запущен!')
main_loop()
