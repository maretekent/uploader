import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from structlog import get_logger

from app_dir.authentication.forms.email_login import EmailForm


logger = get_logger(__name__)


class BaseFormView(FormView):
    """ Base Form class """
    def get(self, request, *args, **kwargs):
        if not requests.session.get("user_email"):
            redirect("/")
        else:
            return super().get(request, *args, **kwargs)


class BaseTemplateview(TemplateView):
    """ Base Template view class"""
    def get(self, request, *args, **kwargs):
        if not request.session.get("user_email"):
            redirect("/")
        else:
            return super().get(request, *args, **kwargs)


class LoginView(BaseTemplateview):
    template_name = "authentication/login.html"
    redirect_url = "/"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data()
        email = self.request.session.get("user_email")
        context["user_email"] = email
        return context

    def post(self, request, *args, **kwargs):

        form = EmailForm(request.POST)
        if not form.is_valid():
            messages.error(request, form.get_error())
            return redirect("check-user-type")

        email = form.cleaned_data["email_address"]
        password = form.cleaned_data("password")

        # email = request.POST.get("email")
        # password = request.POST.get("password")

        if not email:
            messages.error(request, settings.AUTHENTICATION_EMAIL_IS_REQUIRED)
            return redirect("/login")

        if not password:
            messages.error(request, settings.AUTHENTICATION_PASSWORD_IS_REQUIRED)
            return redirect("/login")

        if "next" in request.GET.keys():
            redirect_url = request.GET["next"]

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            redirect(redirect_url)
        else:
            messages.error(request, settings.AUTHENTICATION_INVALID_LOGIN)
            redirect("/login")


@csrf_protect
@require_http_methods(["POST"])
def auto_logout(request):
    """
    :param request: django.http.request.HttpRequest
    :return: django.http.response.HttpResponse
    """

    logger.info("auto-logout-request-start")

    if request.user.is_authenticated:
        messages.warning(request, settings.AUTHENTICATION_AUTOMATIC_LOGOUT_MESSAGE)
        logger.info("auto-logout-request-logout", email=request.user.email)
        logout(request)

    return JsonResponse({"success": True})


def logout_user(request):
    """
    Logs out the logged in user.
    :param request:
    :return:
    """
    logout(request)
    return redirect("/")
