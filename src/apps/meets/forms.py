from django import forms

from apps.meets.models import Meet


class MeetForm(forms.ModelForm):
    class Meta:
        model = Meet
        fields = [
            "title",
            "start_date",
            "start_time",
            "category",
            "responsible",
            "participants",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.TimeInput(attrs={"type": "time"}),
        }
