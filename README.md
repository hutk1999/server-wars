# server-wars

## How To Use:
Run all the servers inside docker containers:

docker-compose up -d --build 

Enter the attack CLI and initiate an attack:

docker exec -it attack_server python attack_server/attack_cli.py

To see how the connection works in real cases, connect to the attack_cli:

docker exec -it attack_server python

Then use 

`import requests`

`x = requests.get('http://reverse_proxy_server:9000/geolocation/topfive', headers={'User-Agent': "Mozilla/5.0 (WindowsCE"})`

`print(x.status_code)`


## P.S.
In a real world example, running `iptables -A OUTPUT -p tcp --tcp-flags ALL RST -j DROP` on the machines would tell the 
kernel not to terminate the connection (by dropping the reset packet), but with the docker I used, it wasn't needed.

I used lower level functionality to prevent the syn_flood attack, since HTTP servers don't get the syn packet, as it 
only receives it after the handshake is finished. 

I made two networks inside the docker compose. The outer network is supposed to be the real world, while the inner 
network is some local network. The only connection between the two networks in the proxy server.


