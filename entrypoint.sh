#!/bin/bash

cd /app

pip install -r requirements.txt 

python manage.py collectstatic --clear --noinput

python manage.py migrate

exec "$@"