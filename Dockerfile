FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive \
	DEBCONF_NONINTERACTIVE_SEEN=true

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y build-essential python3-dev python3 python3-venv python3-pip libpq-dev \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip3 install wheel setuptools \
  && pip3 install django gunicorn psycopg2 dj-database-url pytz whitenoise

RUN useradd -ms /bin/bash runuser

COPY --chown=runuser ./ /app/

USER runuser
WORKDIR /app
EXPOSE 8000

ENTRYPOINT [ "gunicorn", "todo.wsgi", "-b", "0.0.0.0:8000" ]
