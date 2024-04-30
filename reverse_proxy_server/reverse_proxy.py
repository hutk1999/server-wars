from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse, os, random, sys, requests
from io import BytesIO
from socketserver import ThreadingMixIn
import threading
from requests import Response

from reverse_proxy_server.utils.consts import URL_PATH_WHITELIST


def merge_two_dicts(x, y):
    return x | y


def set_header():
    headers = {
        'Host': hostname
    }

    return headers


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_HEAD(self):
        self.do_GET(body=False)
        return

    def do_GET(self, body=True):
        sent = False
        try:
            url = 'http://{}{}'.format(hostname, self.path)
            req_header = self.parse_headers()
            if self.detect_url_brute_force():
                mock_response = self.create_mock_response(url)
                self.send_response(200)
                self.send_resp_headers(mock_response)
            elif detect_http_flood():
                pass
            elif detect_syn_flood():
                pass
            else:
                resp = requests.get(url, headers=merge_two_dicts(req_header, set_header()), verify=False)
                sent = True

                self.send_response(resp.status_code)
                self.send_resp_headers(resp)
                msg = resp.text
                if body:
                    self.wfile.write(msg.encode(encoding='UTF-8', errors='strict'))
                return
        finally:
            if not sent:
                self.send_error(404, 'error trying to proxy')

    def create_mock_response(self, url) -> Response:
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.encoding = 'utf-8'
        mock_response.url = url
        mock_response.raw = BytesIO(b'Evil attack detected')
        return mock_response

    def detect_url_brute_force(self):
        for allowed_path in URL_PATH_WHITELIST:
            if self.path.startswith(allowed_path):
                return False
        return True

    def detect_http_flood(self):
        pass

    def detect_syn_flood(self):
        pass

    def parse_headers(self):
        req_header = {}
        for line in self.headers:
            line_parts = [o.strip() for o in line.split(':', 1)]
            if len(line_parts) == 2:
                req_header[line_parts[0]] = line_parts[1]
        return req_header

    def send_resp_headers(self, resp):
        respheaders = resp.headers
        print('Response Header')
        for key in respheaders:
            if key not in ['Content-Encoding', 'Transfer-Encoding', 'content-encoding', 'transfer-encoding',
                           'content-length', 'Content-Length']:
                print(key, respheaders[key])
                self.send_header(key, respheaders[key])
        self.send_header('Content-Length', len(resp.content))
        self.end_headers()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def reverse_proxy():
    global hostname
    hostname = 'localhost:9000'
    server_address = ('127.0.0.1', 8000)
    httpd = ThreadedHTTPServer(server_address, ProxyHTTPRequestHandler)
    httpd.serve_forever()


reverse_proxy()
