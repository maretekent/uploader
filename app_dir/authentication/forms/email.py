from django import forms
from django.conf import settings


class EmailForm(forms.Form):
    email_address = forms.EmailField(
        required=True,
        error_messages={"required": settings.AUTHENTICATION_EMAIL_IS_REQUIRED},
    )

    def get_error(self):
        """Returns an error encountered during validation

        Picks the first error message found in the self.errors"""

        if self.errors:
            return list(self.errors.values())[0][0]
