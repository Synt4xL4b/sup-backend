from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import TagForm, FeatureForm, ProjectForm, TaskForm
from .models import Tags, Feature


class TagCreateView(generic.CreateView):
    form_class = TagForm
    template_name = 'projects/tags.html'
    success_url = reverse_lazy('projects:index')


class TagUpdateView(generic.UpdateView):
    form_class = TagForm
    template_name = 'projects/tags_update.html'
    success_url = reverse_lazy('projects:index')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Tags, slug=slug)


class FeatureCreateView(generic.CreateView):
    form_class = FeatureForm
    template_name = 'projects/features.html'
    success_url = reverse_lazy('projects:index')



class FeatureUpdateView(generic.UpdateView):
    form_class = FeatureForm
    template_name = 'projects/features_update.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Feature, slug=slug)

    def get_success_url(self):
        return reverse_lazy(self.object.get_absolute_url())


class FeatureDetailView(generic.DetailView):
    queryset = Feature.objects.select_related('tags', 'participants', 'responsible', 'tags').all()
    template_name = 'projects/features_detail.html'
    context_object_name = 'feature'
    slug_url_kwarg = 'slug'


class ProjectListView(generic.ListView):
    pass


class ProjectCreateView(generic.CreateView):
    form_class = ProjectForm
    template_name = 'projects/projects_create.html'
    success_url = reverse_lazy('projects:index')

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(generic.UpdateView):
    form_class = ProjectForm
    template_name = 'projects/projects_update.html'
    success_url = reverse_lazy('projects:index')


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = 'projects/tasks_create.html'
    success_url = reverse_lazy('projects:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    form_class = TaskForm
    template_name = 'projects/tasks_update.html'
    success_url = reverse_lazy('projects:index')
    slug_url_kwarg = 'slug'