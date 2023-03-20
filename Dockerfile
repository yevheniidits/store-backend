FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && \
    apt-get install -y \
    git \
    gdal-bin \
    python3-gdal \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info

WORKDIR /store
COPY requirements.txt /store/

RUN pip install -r /store/requirements.txt --no-cache-dir

EXPOSE 8000
