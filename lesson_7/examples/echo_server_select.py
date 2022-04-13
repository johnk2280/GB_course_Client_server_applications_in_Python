import select
from socket import socket, AF_INET, SOCK_STREAM


def read_request(r_clients: list, all_clients: list) -> dict:
    responses = {}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
            all_clients.remove(sock)

    return responses


def write_responses(requests: dict, w_clients: list, all_clients: list) -> None:
    for sock in w_clients:
        if sock in requests:
            try:
                response = requests[sock].encode('utf-8')
                sock.send(response.upper())
            except:
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился')
                sock.close()
                all_clients.remove(sock)


def main_loop() -> None:
    address = ('', 10000)
    clients = []
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2)
    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print(f"Получен запрос на соединение от {addr}")
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_request(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    print('Эхо-сервер запущен!')
    main_loop()
