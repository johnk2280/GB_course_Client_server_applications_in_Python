import socket
import unittest
import json
import sys

from lesson_5.server.server import MessageServer


class TestMessageServer(unittest.TestCase):

    def test_init(self):
        server = MessageServer('127.0.0.1', 8000)
        self.assertEqual(server.port, 8000)
        self.assertEqual(server.address, '127.0.0.1')
        self.assertEqual(server.sock.family, socket.AF_INET)
        self.assertEqual(server.sock.type, socket.SOCK_STREAM)
        self.assertEqual(server.sock.getsockname(), ('127.0.0.1', 8000))
        server.sock.close()

    def test_get_data(self):
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }
        bytes_data = json.dumps(data).encode('utf-8')

        server = MessageServer('127.0.0.1', 8000)
        self.assertEqual(server.get_data(bytes_data), data)
        server.sock.close()

    def test_create_response(self):
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }
        server = MessageServer('127.0.0.1', 8000)

        self.assertEqual(server.create_response(data), json.dumps({'response': 200}).encode('utf-8'))
        data['action'] = ''
        self.assertEqual(server.create_response(data), json.dumps({'response': 400}).encode('utf-8'))

        server.sock.close()