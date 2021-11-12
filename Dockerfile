FROM python:3-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
RUN mkdir /code/staticfiles

WORKDIR /code

RUN apt-get update \
    && apt-get install -y gdal-bin libgdal-dev python3-gdal binutils libproj-dev

ADD requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

