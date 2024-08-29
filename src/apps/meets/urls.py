from django.urls import path

from apps.meets.views import MeetsView

app_name = "apps.meets"

urlpatterns = [
    # Tag views
    path("", MeetsView.as_view(), name="meets_list"),
]
