FROM ubuntu:latest
COPY . /tp-yaml
WORKDIR /tp-yaml

CMD [ "python", "./application.py" ]
