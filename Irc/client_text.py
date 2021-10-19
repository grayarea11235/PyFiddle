import socket
import sys


def test_connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = ('eu.undernet.org', 6667)
    sock.connect(server_addr)

    sock.sendall('NICK Chickens')


if __name__ == '__main__':
    test_connect()
