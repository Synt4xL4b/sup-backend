from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Category, Meet, MeetParticipant


class MeetsView(LoginRequiredMixin, TemplateView):
    template_name = "meets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["participants"] = MeetParticipant.objects.all()
        context["meets"] = Meet.objects.all()
        return context
