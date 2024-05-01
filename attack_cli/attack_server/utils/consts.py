HOSTNAME = 'reverse_proxy_server'

HOST_IP = '192.168.1.2'

ATTACK_IP = '192.168.1.3'

HOST_PORT = 9000

ATTACK_PORT = 8080

MESSAGE = b'x'*1024

HTTP_FLOOD_REQUEST = f"GET / HTTP/1.1\r\nHost: {HOSTNAME}:{HOST_PORT} \r\n\r\n".encode()
