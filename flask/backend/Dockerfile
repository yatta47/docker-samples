FROM python:3.7-alpine

LABEL version="1.0" \
      maintainer="yatta47"

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    bash \
    git

RUN pip install flask && \
    pip install --upgrade flask

EXPOSE 5000
RUN mkdir /app

ENV APP_PATH=/app
WORKDIR ${APP_PATH}

CMD [ "/bin/sh" ]