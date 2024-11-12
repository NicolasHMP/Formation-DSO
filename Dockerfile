FROM ubuntu:latest

COPY application.py /

CMD [ "python", "./application.py" ]
