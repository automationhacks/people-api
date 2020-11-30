# From blog:
# https://realpython.com/testing-third-party-apis-with-mock-servers/
import json
import re
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):
    USERS_PATTERN = re.compile(r'/users')

    def do_GET(self):
        if re.search(self.USERS_PATTERN, self.path):
            self.send_response(requests.codes.ok)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            response_content = json.dumps([])
            self.wfile.write(response_content.encode('utf-8'))
            return


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port


def start_mock_server(port):
    mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
    # Run tests server in a different thread
    mock_server_thread = Thread(target=mock_server.serve_forever)
    # Daemon threads automatically shut down when the main process exits
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()
