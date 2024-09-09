from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from apps.meets.forms import MeetForm
from apps.meets.models import Category, Meet, User


class MeetsView(LoginRequiredMixin, TemplateView):
    template_name = "meets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["users"] = User.objects.order_by("id")
        context["meets"] = Meet.objects.prefetch_related("participants").all()

        return context


@require_http_methods(["DELETE"])
def delete_meet(request, pk):
    try:
        meet = Meet.objects.get(pk=pk)
        meet.delete()
        return JsonResponse({"success": True})
    except Meet.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "Meet not found"}, status=404
        )


def create_meet(request):
    if request.method == "POST":
        form = MeetForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # Возвращаем успешный ответ
        else:
            return JsonResponse(
                {"success": False, "error": form.errors}, status=400
            )  # Возвращаем ошибки
    return JsonResponse(
        {"success": False, "error": "Invalid request"}, status=400
    )
