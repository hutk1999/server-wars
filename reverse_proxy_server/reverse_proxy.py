import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

import requests
from requests import Response

from utils.consts import URL_PATH_WHITELIST, USER_AGENTS, HEADER_KEYS, HOSTNAME, SERVER_IP, SERVER_PORT


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_HEAD(self) -> None:
        self.do_GET(body=False)
        return

    def do_GET(self, body=True) -> None:
        global server_logger
        sent = False
        try:
            url = f'http://{hostname}{self.path}'
            server_logger.info("Got GET request", extra={"values": url})
            if not self.unsafe_request():
                server_logger.info("No malicious activities detected", extra={"values": url})
                response = requests.get(url, headers={'Host': hostname}, verify=False)
                sent = True
                server_logger.info("Received server response", extra={"values": response.status_code})
                self.response_handler(response, body)
                server_logger.info("Returned response to user", extra={"values": self.client_address})
                return

        finally:
            if not sent:
                # self.send_error(200, 'Evil attack detected')
                server_logger.info("Malicious activities detected", extra={"values": url})

    def unsafe_request(self) -> bool:
        return self.detect_url_brute_force() or self.detect_http_flood()

    def detect_url_brute_force(self) -> bool:
        global server_logger
        for allowed_path in URL_PATH_WHITELIST:
            if self.path.startswith(allowed_path):
                server_logger.info("Whitelisted URL", extra={"values": self.path})
                return False
        server_logger.info("Detected non whitelisted URL", extra={"values": self.path})
        return True

    def detect_http_flood(self) -> bool:
        global server_logger
        for allowed_user_agent in USER_AGENTS:
            if self.headers.get('User-Agent').startswith(allowed_user_agent):
                server_logger.info("Whitelisted user-agent", extra={"values": self.headers.get('User-Agent')})
                return False
        server_logger.info("Detected non whitelisted user-agent", extra={"values": self.headers.get('User-Agent')})
        return True

    def response_handler(self, response: Response, body: bool) -> None:
        self.send_response(response.status_code)
        self.send_response_headers(response)
        message = response.text
        if body:
            self.wfile.write(message.encode(encoding='UTF-8', errors='strict'))

    def send_response_headers(self, response: Response) -> None:
        response_headers = response.headers
        for key in response_headers:
            if key not in HEADER_KEYS:
                self.send_header(key, response_headers[key])
        self.send_header('Content-Length', len(response.content))
        self.end_headers()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def reverse_proxy() -> None:
    global hostname
    global server_logger
    hostname = HOSTNAME
    server_address = (SERVER_IP, SERVER_PORT)
    server_logger.info("Starting reverse proxy server", extra={"values": server_address})
    httpd = ThreadedHTTPServer(server_address, ProxyHTTPRequestHandler)
    httpd.serve_forever()


logging.basicConfig(filename='reverse_proxy_logger.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(values)s')
server_logger = logging.getLogger('reverse_proxy_server')
reverse_proxy()
