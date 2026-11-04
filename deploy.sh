#!/bin/bash

NAME="printobserver_camera_service"

echo "Stopping old container..."

docker rm -f $NAME 2>/dev/null

echo "Building image..."

docker build \
  -t $NAME .

echo "Starting container..."

docker run \
  -d \
  --restart=always \
  --name $NAME \
  -v /home/printobserver/data:/data \
  $NAME

echo "Container logs:"

docker logs -f $NAME