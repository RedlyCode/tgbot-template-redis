FROM python:3.11
ENV BOT_NAME=tgbot

WORKDIR /usr/src/app/"${BOT_NAME}"

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
