FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    curl \
    python3 \
    python3-pip \
    python3-mapnik \
    mapnik-utils \
    fontconfig \
    fonts-noto \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    fonts-hanazono \
    && fc-cache -fv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install fastapi uvicorn jupyter
# RUN pip install fastapi uvicorn jupyter --break-system-packages
