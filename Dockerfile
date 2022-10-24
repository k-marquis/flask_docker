FROM python:3.10.5-slim-buster
LABEL author="Kris Marquis <krismarquis86@gmail.com"

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /pomoapp
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "pomoapp.app:create_app()"
