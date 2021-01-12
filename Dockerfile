FROM python:3.7.4

RUN set -ex \
    && apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    libgeos-dev

ADD requirements.txt /root/requirements.txt

ADD ./api /interview
WORKDIR /root

RUN pip install --upgrade pip
RUN pip install -r /root/requirements.txt

WORKDIR /interview

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
