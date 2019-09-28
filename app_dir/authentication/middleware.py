from time import time

from django.conf import settings
from django.contrib.auth import logout
from structlog import get_logger

logger = get_logger(__name__)


def auto_logout_middleware(get_response):
    def middleware(request):
        if not request.user.is_authenticated:
            request.session.pop(
                settings.AUTHENTICATION_LAST_ACCESS_TIMESTAMP_SESSION_KEY, None
            )

        else:
            last_access_timestamp = request.session.get(
                settings.AUTHENTICATION_LAST_ACCESS_TIMESTAMP_SESSION_KEY
            )

            if last_access_timestamp:
                if (
                    time() - last_access_timestamp
                ) > settings.AUTHENTICATION_IDLE_TIMEOUT_IN_SECONDS:
                    logout(request)

            new_timestamp = time()

            request.session[
                settings.AUTHENTICATION_LAST_ACCESS_TIMESTAMP_SESSION_KEY
            ] = new_timestamp

        return get_response(request)

    return middleware
