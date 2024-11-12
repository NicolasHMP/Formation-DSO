#FROM python:3.9-slim
FROM python:3.6-windowsservercore
WORKDIR /application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "application.py" ]