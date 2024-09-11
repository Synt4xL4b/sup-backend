from django import forms

from apps.meets.models import Category, User


class CreateMeetForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["users"].initial = forms.ModelMultipleChoiceField(
    #         queryset=User.objects.all()
    #     )

    title = forms.CharField()
    start_date = forms.DateField()
    start_time = forms.TimeField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    author = User.objects.get(pk=1)
    responsible = forms.ModelChoiceField(queryset=User.objects.all())
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    # class Meta:
    #     model = Meet
    #     fields = [
    #         "title",
    #         "start_date",
    #         "start_time",
    #         "category",
    #         "responsible",
    #         # "participants",
    #     ]
    #     widgets = {
    #         "start_date": forms.DateInput(attrs={"type": "date"}),
    #         "start_time": forms.TimeInput(attrs={"type": "time"}),
    #     }
