FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    dbus-dev \
    dbus \
    glib-dev \
    pkgconfig \
    python3-dev \
    py3-setuptools \
    py3-wheel \
    py3-pip \
    meson \
    libvirt-dev \
    pkgconfig \
    libxml2-dev \
    libxslt-dev

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

WORKDIR /app/src

ENTRYPOINT ["python", "app.py"]
