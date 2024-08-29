from django import forms

from apps.projects.models import Feature, Project, Tags, Task

from apps.projects.choice_classes import ProjectChoices
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ["name", "color"]


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = [
            "name",
            "responsible",
            "description",
            "tags",
            "participants",
            "importance",
            "status",
        ]


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "participants",
            "status",
            "created_at"
        ]

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-500 w-full',
            'placeholder': 'Введите название проекта'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'editor mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-500 w-full',
            'placeholder': 'Описание проекта'
        }
    ))
    status = forms.ChoiceField(
        choices=ProjectChoices,
        widget=forms.Select(attrs={
            'id': 'project-status',
            'class': 'mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-500 w-full'
        }),
        required=True
    )
    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_superuser=True),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    created_at = forms.DateField(initial=timezone.now, widget=forms.TextInput(
        attrs={
            'class': 'mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-teal-500 w-full',
            'type': 'date'
        }
    ))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "feature",
            "description",
            "tags",
            "participants",
            "importance",
            "date_execution",
            "status",
        ]
