from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.users.forms import CustomUserForm


class SignUpView(CreateView):
    template_name = "reg.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserForm
    success_message = "Профиль был успешно создан."
