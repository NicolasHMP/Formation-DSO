FROM ubuntu:latest
COPY . /tp-yaml
WORKDIR /tp-yaml


EXPOSE 1234
CMD [ "/application.py" ]