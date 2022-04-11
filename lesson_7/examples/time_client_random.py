from socket import socket, AF_INET, SOCK_STREAM


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 8888))

while True:
    tm = sock.recv(1024)
    print(f'Current time: {tm.decode("utf-8")}')

socket.close()
