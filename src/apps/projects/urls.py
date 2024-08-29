from django.urls import path

from apps.projects.views import (
    FeatureCreateView,
    FeatureUpdateView,
    ProjectCreateView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
    TaskUpdateView,
    ProjectListView
)

app_name = "apps.projects"

urlpatterns = [
    # Project views
    path("", ProjectListView.as_view(), name="list_projects"),
    path("create-project/", ProjectCreateView.as_view(), name="create_project"),

]
