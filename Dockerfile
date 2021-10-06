FROM python:3.6

# RUN apt-get update -y

ADD . /opt/working
WORKDIR "/opt/working"

RUN pip install -r requirements.txt