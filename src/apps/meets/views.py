from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Category, Meet, User


class MeetsView(LoginRequiredMixin, TemplateView):
    template_name = "meets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["users"] = User.objects.order_by("id")
        context["meets"] = Meet.objects.prefetch_related("participants").all()

        return context
