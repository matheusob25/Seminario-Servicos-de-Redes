FROM alpine:latest

RUN apk --no-cache add curl

# sudo docker build -t app_container -f app_container.dockerfile .  
# sudo docker run -d --name app_container_1 app_container tail -f /dev/null
