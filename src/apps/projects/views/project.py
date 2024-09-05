from django.urls import reverse_lazy
from django.views import generic

from apps.projects.forms import ProjectForm

from apps.projects.models import Project


class ProjectListView(generic.ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/project.html"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Project.objects.filter(name__icontains=query)
        return Project.objects.all().order_by('-created_at')

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['form'] = ProjectForm
        context['query'] = self.request.GET.get('query', '')
        return context



class ProjectCreateView(generic.CreateView):
    form_class = ProjectForm
    template_name = "projects/project.html"
    success_url = reverse_lazy("projects:list_projects")

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        return super().form_valid(form)
