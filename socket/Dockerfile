FROM node:12
RUN mkdir /app
WORKDIR /app

RUN npm install
EXPOSE 8888

CMD ["node","index.js"]
COPY ./node/ /app
