FROM --platform=linux/amd64 python:3.10-slim

# よく使うコマンドをインストール
RUN apt update \
  && apt install -y wget zip curl

# コンテナを起動しつづけるためのcrondを使いたいのでインストール
RUN apt install -y cron

# lambdaのローカル実行のために、AWS CLIをインストール
RUN wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O awscliv2.zip \
  && unzip awscliv2.zip \
  && ./aws/install

WORKDIR /var/app

# pip install
RUN pip install --upgrade pip
COPY ./requirements.txt /var/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest python-lambda-local

# コンテナを起動しつづけるために、crondを起動
CMD ["cron", "-f"]
