#!/bin/bash

cat pyproject.toml
cd ./cloud_project
poetry run python manage.py makemigrations
poetry run python manage.py migrate
# poetry run python manage.py createsuperuser
# poetry run python manage.py runserver 0.0.0.0:8000
gunicorn cloud_project.wsgi:application --bind 0.0.0.0:8000