from django import forms

from webapp.models import Mission, Status, Type, Project


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        exclude = ['created_at', 'updated_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']



class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created_at', 'updated_at']

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
