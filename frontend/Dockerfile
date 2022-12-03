# stage 1
FROM node:19-alpine as builder

WORKDIR /app

COPY package*.json .
RUN npm install

COPY . .

RUN npm run build

# stage 2
FROM nginx:1.23-alpine as production-build

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist/ /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 8080
ENTRYPOINT ["nginx", "-g", "daemon off;"]