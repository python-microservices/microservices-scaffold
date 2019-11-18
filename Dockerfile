FROM python:3.6.4-alpine3.7

RUN apk add --update curl gcc g++ git libffi-dev openssl-dev python3-dev build-base linux-headers \
    && rm -rf /var/cache/apk/*
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV PYTHONUNBUFFERED=1 ENVIRONMENT=pre APP_HOME=/microservice/
ENV DATABASE_DIR=database
ENV CONFIGMAP_FILE="$APP_HOME"config-docker.yml

RUN mkdir $APP_HOME && adduser -S -D -H python
RUN chown -R python $APP_HOME
WORKDIR $APP_HOME

ADD requirement*.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements-docker.txt

ADD . $APP_HOME
RUN mkdir $DATABASE_DIR
RUN chmod 777 $DATABASE_DIR

EXPOSE 5000
USER python

CMD ["gunicorn", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "manage:app"]