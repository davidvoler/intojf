ARG TAG="LOCAL"
FROM node:18.14.1-slim as builder

RUN mkdir /ngapp
WORKDIR /ngapp
COPY frontend/package.json .
RUN npm install 

COPY ./ui/ .

RUN npm build

FROM nginx:stable-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /ngapp/dist/  /usr/share/nginx/html/
CMD ["nginx", "-g", "daemon off;"]