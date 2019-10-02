from django.urls import path
from app_dir.authentication.views import (
    auto_logout,
    LoginView,
    logout,
    ResendPasswordLinkView,
)

urlpatterns = [
    path("auto-logout", auto_logout, name="auto-logout"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout, name="logout"),
    path("resend-link", ResendPasswordLinkView.as_view(), name="resend-link"),
]
