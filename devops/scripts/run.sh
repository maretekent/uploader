#!/usr/bin/env bash
set -e
python manage.py migrate --no-input

## create super_user
python manage.py shell << EOF
from os import environ
from django.contrib.auth.models import User
username=environ.get('DEV_LOGIN_USERNAME')
password=environ.get('DEV_LOGIN_PASSWORD')
email=environ.get('DEV_LOGIN_EMAIL', 'devopske@jumo.world')
if username is None and password is None:
    print("DEV_LOGIN_USERNAME & DEV_LOGIN_PASSWORD env. vars not provided.")
else:
    User.objects.filter(username=username).delete()
    User.objects.create_superuser(username, email, password)
EOF

python manage.py runserver 0.0.0.0:80

