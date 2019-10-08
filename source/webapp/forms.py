from django import forms

from webapp.models import Mission, Status,Type


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
