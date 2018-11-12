FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .