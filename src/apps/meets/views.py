from django.views.generic import TemplateView

from .models import Meet, MeetParticipant


class MeetsView(TemplateView):
    template_name = "meets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["participants"] = MeetParticipant.objects.all()
        context["meets"] = Meet.objects.all()
        return context
