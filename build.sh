#!/bin/bash
docker build -t server src/
docker build -t client client/
docker run -d -p 5000:5000 --name server server
docker run -it --link server:client --name clientest client bash
