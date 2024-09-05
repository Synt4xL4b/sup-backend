from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from apps.projects.forms import FeatureForm
from apps.projects.models import Feature


class FeatureListView(generic.ListView):
    model = Feature
    template_name = 'projects/fitch.html'
    context_object_name = 'features'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['form'] = ''
        context['query'] = self.request.GET.get('query', '')
        return context
