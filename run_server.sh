#!/bin/bash

cd ./cloud_project
poetry run python manage.py makemigrations
poetry run python manage.py migrate
# poetry run python manage.py createsuperuser
poetry run python manage.py runserver 0.0.0.0:8000