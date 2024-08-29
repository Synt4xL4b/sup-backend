from django.urls import path

from apps.meets.views import MeetsView

app_name = "apps.meets"

urlpatterns = [
    path("", MeetsView.as_view(), name="meets"),
]
