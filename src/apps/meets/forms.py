from django import forms

from apps.meets.models import Category, User


class CreateMeetForm(forms.Form):
    title = forms.CharField()
    start_date = forms.DateField()
    start_time = forms.TimeField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    author = User.objects.get(pk=1)
    responsible = forms.ModelChoiceField(queryset=User.objects.all())
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())
