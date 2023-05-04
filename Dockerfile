FROM python:3.10-slim-buster

RUN apt update

RUN apt install wget gnupg -y

RUN wget -q https://ftp-master.debian.org/keys/release-10.asc -O- | apt-key add -
RUN echo "deb http://deb.debian.org/debian buster non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install  libttspico-utils -y

RUN pip install -U so-vits-svc-fork


RUN pip install gradio

WORKDIR /app

COPY main.py /app

ENTRYPOINT ["python3", "main.py"]
