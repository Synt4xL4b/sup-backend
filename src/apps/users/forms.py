from django.forms import ModelForm

from apps.users.models import CustomUser, Permissions, Role


class CustomUserForm(ModelForm):
    """Форма модели CustomUser."""

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "surname",
            "email",
            "tg_name",
            "tg_nickname",
            "google_meet_nickname",
            "gitlab_nickname",
            "github_nickname",
            "role",
            "avatar",
            "role",
            "permissions",
        ]


class RoleForm(ModelForm):
    """Форма модели Role."""

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
