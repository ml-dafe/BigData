FROM python:3.6.1
MAINTAINER Kirill Vlasov <vlasoff.k@gmail.com>

RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src /src
WORKDIR /src


CMD [ "python", "./main.py" ]