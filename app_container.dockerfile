FROM alpine:latest

RUN apk --no-cache add curl

# sudo docker build -t app_container -f app_container.dockerfile .  