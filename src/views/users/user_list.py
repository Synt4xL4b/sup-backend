from django.views.generic.list import ListView

from apps.users.forms import ListUserForm
from apps.users.models import CustomUserList


class UserListView(ListView):
    """Представление для просмотра списка пользователей с фильтрацией по ролям ."""

    model = CustomUserList
    paginate_by = 50
    template_name = "UserTable.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        role = self.request.GET.get("role")
        if role:
            queryset = queryset.filter(role=role)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter-form"] = ListUserForm(self.request.GET)
        return context
