from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import MissionForm, StatusForm, TypeForm
from webapp.models import Mission, Type
from django.views import View
from django.views.generic import ListView,CreateView
from .base_view import DetailView, UpdateView, DeleteView


class TypeIndexView(ListView):
    template_name = 'type/type.html'
    context_object_name = 'types'
    model = Type
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Type.objects.all()



class TypeView(DetailView):

    template_name = 'type/type_view.html'
    model = Type
    context_object = 'type'
    context_key = 'type'

class TypeCreateView(CreateView):

    template_name = 'type/create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})

class TypeUpdateView(UpdateView):
    form = TypeForm
    template = 'type/update.html'
    model = Type
    context_key = 'type'
    context_object = 'type'
    context_form = 'form'
    redirect_url = 'type_view'

class TypeDeleteView(DeleteView):
    model = Type
    template = 'type/delete.html'
    redirect_url = 'index'
    context_object =  'type'
    context_key = 'type'
    confirm_deletion = False

