FROM alpine:latest

WORKDIR /root

ADD requirements.txt requirements.txt
ADD src src

RUN set -x && \
    apk update && \
    apk add python3 && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD /bin/sh
