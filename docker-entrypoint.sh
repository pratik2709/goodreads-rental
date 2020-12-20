#!/bin/bash
python manage.py collectstatic --noinput
python manage.py makemigrations rent_engine --noinput
python manage.py migrate --noinput
python manage.py loaddata rent_engine/fixtures/data.json
python manage.py loaddata rent_engine/fixtures/customer.json
python manage.py loaddata rent_engine/fixtures/version_3.json
python manage.py load_data
gunicorn goodreads.wsgi:application --bind 0.0.0.0:8000

