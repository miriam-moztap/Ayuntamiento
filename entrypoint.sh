#!/bin/bash

cd /app/Apps

pip install -r requirements.txt 

python manage.py collectstatic --clear --noinput

python manage.py migrate

exec "$@"