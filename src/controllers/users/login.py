from django.views.generic import TemplateView

from apps.users.forms import CustomUserForm


class UserLogin(TemplateView, CustomUserForm):
    template_name = "index.html"
