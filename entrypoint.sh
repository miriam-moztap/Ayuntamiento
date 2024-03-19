#!/bin/bash

cd /app

pip install -r requirements.txt 

python manage.py collectstatic --clear --noinput

python manage.py migrate

#Iniciar Gunicorn
exec gunicorn Apps.ayunt.wsgi:application --bind 0.0.0.0.0:8000