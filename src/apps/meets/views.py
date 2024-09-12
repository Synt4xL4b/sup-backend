from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from apps.meets.forms import CreateMeetForm
from apps.meets.models import Category, Meet, User


class MeetsView(LoginRequiredMixin, TemplateView):
    template_name = "meets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["users"] = User.objects.order_by("id")
        context["meets"] = Meet.objects.prefetch_related("participants").all()

        return context


@require_POST
def delete_meet(request, meet_id):
    try:
        meet = get_object_or_404(Meet, id=meet_id)
        meet.delete()
        return JsonResponse({"status": "success"})
    except Meet.DoesNotExist:
        return JsonResponse({"status": "Meet not found"}, status=404)


class CreateMeetView(LoginRequiredMixin, View):
    """
    Создание мита
    """

    def get(self, request):
        form = CreateMeetForm()
        categories = Category.objects.all()
        return render(
            request,
            "create_meet_modal.html",
            {"form": form, "categories": categories},
        )

    def post(self, request):
        form = CreateMeetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            meet = Meet.objects.create(
                author=request.user,
                title=data["title"],
                start_date=data["start_date"],
                start_time=data["start_time"],
                category=data["category"],
                responsible=data["responsible"],
            )

            pprint(form.cleaned_data["participant_statuses"])
            # Добавляем участников
            meet.participants.set(data["participants"])
            for user in form.cleaned_data["participant_statuses"].items():
                meet.participants.set([user])

            for part in meet.participants.all():
                pprint(part)

            meet.save()

            return JsonResponse({"status": "success"}, status=201)

        return render(request, "create_meet_modal.html", {"form": form})
