FROM ubuntu:16.04

MAINTAINER "Sateesh Kumar"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt
RUN pip3 install requests

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
