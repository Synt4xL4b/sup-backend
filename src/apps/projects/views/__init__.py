__all__ = (
    "FeatureCreateView",
    "FeatureUpdateView",
    "ProjectCreateView",
    "ProjectUpdateView",
    "TagCreateView",
    "TagUpdateView",
    "TaskCreateView",
    "TaskUpdateView",
)

from apps.projects.views.feature import FeatureCreateView, FeatureUpdateView
from apps.projects.views.project import ProjectCreateView, ProjectListView
from apps.projects.views.tags import TagCreateView, TagUpdateView
from apps.projects.views.task import TaskCreateView, TaskUpdateView
