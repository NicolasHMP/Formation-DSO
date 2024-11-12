FROM python:latest
WORKDIR /application
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "application.py" ]