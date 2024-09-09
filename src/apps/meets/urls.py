from django.urls import path

from apps.meets.views import MeetsView, create_meet, delete_meet

app_name = "apps.meets"

urlpatterns = [
    path("", MeetsView.as_view(), name="meets"),
    path("delete/<int:pk>/", delete_meet, name="delete_meet"),
    path("create/", create_meet, name="create_meet"),
]
