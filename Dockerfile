FROM ubuntu:latest
COPY . /
EXPOSE 1234
CMD [ "application.py" ]