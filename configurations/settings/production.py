from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

configure_structlog("production")
