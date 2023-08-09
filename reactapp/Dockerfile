ARG NODE_VERSION=18
FROM node:${NODE_VERSION}-alpine as builder
WORKDIR /app
COPY ./reactapp/package*.json /app/
RUN npm install
COPY ./reactapp /app
RUN npm run build


FROM node:${NODE_VERSION}-alpine
WORKDIR /app
RUN npm install -g serve
COPY --from=builder /app/build ./build