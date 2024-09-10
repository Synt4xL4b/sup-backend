from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.users.models import CustomUser
from validators.validators import PasswordValidator


class ChangePasswordView(LoginRequiredMixin, TemplateView):
    """Представление для изменения пароля пользователю."""

    template_name = "password.html"
    success_url = reverse_lazy("user_list")

    def post(self, request, *args, **kwargs):
        old_password: str = request.POST.get("old_password")
        new_password1: str = request.POST.get("new_password1")
        new_password2: str = request.POST.get("new_password2")

        user: CustomUser = request.user

        if not user.check_password(old_password):
            messages.error(request, "Неверный пароль")
            return redirect("password")

        if len(new_password1) < 8:
            messages.error(
                request, "Пароль должен содержать минимум 8 символов."
            )
            return redirect("password")

        if new_password1 == old_password:
            messages.error(
                request, "Новый пароль не может совпадать с предыдущим."
            )
            return redirect("password")

        if new_password1 != new_password2:
            messages.error(request, "Пароли должны совпадать.")
            return redirect("password")

        try:
            PasswordValidator.get_regex_validator(new_password1)
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect("password")

        user.set_password(new_password1)
        user.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Пароль успешно изменен.")
        return redirect("user_list")
