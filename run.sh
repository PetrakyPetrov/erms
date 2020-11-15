#!/bin/bash

docker-compose up -d --build
docker-compose run internal_system python3 /var/www/html/internal_system/manage.py makemigrations
docker-compose run internal_system python3 /var/www/html/internal_system/manage.py migrate
# docker restart hr_system