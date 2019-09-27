from django import forms
from django.forms import widgets

from webapp.models import Status,Type


class MissionForm(forms.Form):

    summary  = forms.CharField(max_length=200, label='Summary', required=True)

    description  = forms.CharField(max_length=3000, label='Description', required=True,
                           widget=widgets.Textarea)

    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Status',
                                      empty_label=None)

    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, label='Type',
                                      empty_label=None)