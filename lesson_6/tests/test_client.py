import json
import unittest

from lesson_6.client.client import Client, parse_command_line
from lesson_6.server.server import MessageServer


class TestClient(unittest.TestCase):

    def test_create_message(self):
        server = MessageServer('127.0.0.1', 8888)
        client = Client('127.0.0.1', 8888)
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }

        self.assertEqual(client.create_message(),
                         json.dumps(data).encode('utf-8'))
        client.sock.close()
        server.sock.close()

    def test_send_request(self):
        server = MessageServer('127.0.0.1', 8888)
        client = Client('127.0.0.1', 8888)
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }

        self.assertEqual(client.send_request(json.dumps(data).encode('utf-8')),
                         None)
        client.sock.close()
        server.sock.close()

    def test_get_response(self):
        server = MessageServer('127.0.0.1', 8888)
        client = Client('127.0.0.1', 8888)
        data = {
            "action": "presence",
            "time": '',
            "type": "status",
            "user": {
                "account_name": "C0deMaver1ck",
                "status": "Yep, I am here!",
            }
        }

        self.assertEqual(client.get_response(json.dumps(data).encode('utf-8')),
                         data)
        client.sock.close()
        server.sock.close()
