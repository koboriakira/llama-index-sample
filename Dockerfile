FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /var/app

# pip install
RUN pip install --upgrade pip
COPY ./requirements.txt /var/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
