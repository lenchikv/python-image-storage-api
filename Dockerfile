FROM python:3.8.2-slim AS base

ENV PIP_NO_CACHE_DIR=true
ENV PYTHONUNBUFFERED=1

RUN mkdir /photos_storage
WORKDIR /photos_storage
COPY requirements.txt /photos_storage/
RUN pip install -r requirements.txt
COPY . /photos_storage/

FROM base AS dev
RUN python -m pip install -r requirements.dev.txt --no-cache-dir
