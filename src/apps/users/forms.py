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

    role = forms.ChoiceField(
        choices=[("Admin, admin"), ("User", "user")], required=False
    )

    class Meta:
        model = CustomUserList
        fields = [
            "id",
            "name",
            "surname",
            "email",
            "tg_name",
            "tg_nickname",
            "google_meet_nickname",
            "gitlab_nickname",
            "github_nickname",
            "registration_date",
            "is_active",
        ]


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
