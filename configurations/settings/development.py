from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "s3upload",
        "USER": "s3upload",
        "PASSWORD": "s3upload",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

INSTALLED_APPS = INSTALLED_APPS + ["corsheaders", "django_extensions"]

configure_structlog("development")
