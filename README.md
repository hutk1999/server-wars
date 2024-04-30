# server-wars

## How To:
Run all the servers inside docker containers:
docker-compose up -d --build 

Enter the attack CLI and initiate an attack:
docker exec -it attack_server python attack_server/attack_cli.py






## P.S.
In a real world example, running `iptables -A OUTPUT -p tcp --tcp-flags ALL RST -j DROP` on the machines would tell the 
kernel not to terminate the connection (by dropping the reset packet), but with the docker I used, it wasn't needed


