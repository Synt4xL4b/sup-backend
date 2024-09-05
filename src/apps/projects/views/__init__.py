__all__ = (
    "ProjectCreateView",
    "ProjectUpdateView",
    'FeatureListView',
)

from apps.projects.views.feature import FeatureListView
from apps.projects.views.project import ProjectCreateView, ProjectListView