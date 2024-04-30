FROM python:3.11

WORKDIR /server

COPY .. /server

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python /server/main.py
