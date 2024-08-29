from django.views import generic

from apps.projects.forms import ProjectForm


class MeetsView(generic.CreateView):
    """
    Контроллер с таблицей митов
    """

    form_class = ProjectForm
    template_name = "meets.html"

    def form_valid(self, form):
        form.instance.responsible = self.request.user
        return super().form_valid(form)
