from django import forms
from django.contrib.auth.models import User

from webapp.models import Mission, Status, Type, Project, Team


class MissionForm(forms.ModelForm):

    class Meta:
        model = Mission
        exclude = ['created_at', 'updated_at','created_by','project']

        widgets = {
            'description': forms.Textarea
        }

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project')
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'] = forms.ModelChoiceField(queryset=User.objects.filter(
            participant__project=self.project)
        )




class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']



class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']

class ProjectForm(forms.ModelForm):

    user = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
