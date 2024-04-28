URLBUSTER_COMMMAND = 'urlbuster -W attack_server/utils/wordlist.txt http://localhost:8000/'

HOST_IP = '127.0.0.1'

ATTACK_IP = '0.0.0.0'

HOST_PORT = 8000

ATTACK_PORT = 8080

MESSAGE = b'x'*1024

HTTP_FLOOD_REQUEST = f"GET / HTTP/1.1\nHost: {HOST_IP}:{HOST_PORT} \n\n".encode()
