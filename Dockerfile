FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update \
    && apt-get -y install libpq-dev gcc libcurl4-openssl-dev libssl-dev

COPY requirements.txt /code/

RUN pip install -r requirements.txt
RUN apt autoremove -y