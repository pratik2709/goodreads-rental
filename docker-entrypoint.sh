#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn goodreads.wsgi:application --bind 0.0.0.0:8000

