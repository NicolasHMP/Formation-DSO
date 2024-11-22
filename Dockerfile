FROM python:3.9-slim
#FROM python:3.6-windowsservercore
#FROM mcr.microsoft.com/windows/servercore:ltsc2022
#RUN powershell -Command \
#  Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile python-installer.exe; \
#  Start-Process python-installer.exe -ArgumentList '/quit InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait;\
#  Remove-Item -Force python-installer.exe
  
#RUN python --version; powershell -Command "Write-Host 'PowerShell ready'"

WORKDIR /application
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "application.py" ]