FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add --no-cache uwsgi uwsgi-python3 uwsgi-http bash curl \
    && pip3 install --no-cache-dir -r requirements.txt -t /usr/lib/python3.8/site-packages

COPY . /usr/src/app

EXPOSE 8080

CMD [ "uwsgi", "--http-socket", "0.0.0.0:8080", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "app:application" ]