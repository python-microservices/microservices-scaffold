FROM python:3.6.4-alpine3.7

RUN apk add --update curl gcc g++ libffi-dev openssl-dev python3-dev \
    && rm -rf /var/cache/apk/*
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV PYTHONUNBUFFERED=1 ENVIRONMENT=pre APP_HOME=/microservice/

RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD requirement*.txt $APP_HOME
RUN pip install -r requirements-docker.txt
ADD . $APP_HOME

EXPOSE 5000

CMD ["gunicorn", "--worker-class", "eventlet", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "manage:app"]