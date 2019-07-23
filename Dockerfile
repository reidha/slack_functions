FROM alpine:latest

WORKDIR /root

COPY requirements.txt requirements.txt
COPY src src

RUN set -x && \
    apk update && \
    apk add python3 && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    mkdir /var/run/sf

CMD ["python3", "src/main.py"]
