from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "s3upload",
        "USER": "root",
        "PASSWORD": "admin123",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

INSTALLED_APPS = INSTALLED_APPS + ["corsheaders", "django_extensions"]

configure_structlog("development")
