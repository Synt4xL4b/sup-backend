from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.users.forms import CustomUserForm


class UserLogin(TemplateView, CustomUserForm):
    """Представление для авторизации пользователя."""

    template_name = "index.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserForm
    success_message = "Вы успешно вошли."
