FROM node:12
RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install cron
RUN npm install
EXPOSE 8888

ADD crontab /etc/cron.d/cronPush
RUN chmod 0644 /etc/cron.d/cronPush

RUN crontab /etc/cron.d/cronPush

CMD ["node","index.js"]
COPY ./node/ /app
