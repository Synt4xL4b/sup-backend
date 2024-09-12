from django import forms
from django.forms import ModelForm

from apps.users.models import CustomUser, CustomUserList, Permissions, Role


class CustomUserForm(ModelForm):
    """Форма модели CustomUser."""

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "surname",
            "password",
            "email",
            "tg_name",
            "tg_nickname",
            "google_meet_nickname",
            "gitlab_nickname",
            "github_nickname",
            "role",
            "avatar",
            "permissions",
        ]


class ListUserForm(ModelForm):
    """Форма для просмотра списка пользователей."""

    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        required=False,
        label="Роль",
        help_text="Выберите роль пользователя",
    )
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        required=True,
        label="Пользователь",
        help_text="Выберите пользователя",
    )

    class Meta:
        model = CustomUserList
        exclude = ["avatar", "permissions"]


class RoleForm(ModelForm):
    """Форма модели Role."""

    class Meta:
        model = Role
        fields = [
            "name",
            "color",
        ]


class PermissionsForm(ModelForm):
    """Форма модели Permissions."""

    class Meta:
        model = Permissions
        fields = [
            "name",
            "code",
            "description",
        ]
