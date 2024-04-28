URLBUSTER_COMMMAND = 'urlbuster -W attack_server/utils/wordlist.txt http://localhost:8000/'

HOST_IP = '10.10.0.2'

ATTACK_IP = '10.10.0.3'

HOST_PORT = 8000

ATTACK_PORT = 8080

MESSAGE = b'x'*1024

HTTP_FLOOD_REQUEST = f"GET / HTTP/1.1\r\nHost: {HOST_IP}:{HOST_PORT} \r\n\r\n".encode()
