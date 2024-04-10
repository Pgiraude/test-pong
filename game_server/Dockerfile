FROM python:3.12
ENV PYTHONUNBUFFERED 1 
ENV DOCKERIZE_VERSION v0.6.1
WORKDIR /app

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY requirements.txt /app/requirements.txt
run pip install -r requirements.txt
COPY . /app
