from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.users.forms import CustomUserForm


class SignUpView(CreateView):
    """Представление для создания пользователя."""

    template_name = "reg.html"
    success_url = reverse_lazy("user_list")
    form_class = CustomUserForm
    success_message = "Профиль был успешно создан."
