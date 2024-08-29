from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("apps.projects.urls", namespace="projects")),
    path("meets/", include("apps.meets.urls", namespace="meets")),
]
