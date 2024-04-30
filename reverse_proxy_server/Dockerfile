FROM python:3.11

WORKDIR /server

COPY .. /server

RUN pip install -r requirements.txt

EXPOSE 9000

CMD bash echo 1 > /proc/sys/net/ipv4/tcp_syncookies

CMD bash echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog

CMD bash echo 3 > /proc/sys/net/ipv4/tcp_synack_retries

CMD python /server/reverse_proxy.py
