#!/bin/bash

# Define the directory path to recursively iterate
DIRECTORY_PATH=.

# Define the Docker Compose configuration file
DOCKER_COMPOSE_FILE=docker-compose.yml

# Remove the Docker Compose file if it already exists
if [ -f $DOCKER_COMPOSE_FILE ]; then
    rm $DOCKER_COMPOSE_FILE
fi

# Remove the Docker Compose file if it already exists
if [ -f $DOCKER_COMPOSE_FILE ]; then
    rm $DOCKER_COMPOSE_FILE
fi

# Open the Docker Compose file for writing
touch $DOCKER_COMPOSE_FILE

# Start the Docker Compose file with the version and services sections
echo "version: '3.9'
services:
  app:
    volumes:" >> $DOCKER_COMPOSE_FILE

# Recursively iterate the directories and add them as volume paths in Docker Compose
declare -A added_dirs
for dir in $(find $DIRECTORY_PATH -type d); do
    dir_name=$(basename $dir)
    if [ "$dir_name" != "node_modules" ] && [ ! ${added_dirs["$dir"]} ]; then
        echo "      - $dir:/app/$dir_name:z" >> $DOCKER_COMPOSE_FILE
        added_dirs["$dir"]=true
    fi
done