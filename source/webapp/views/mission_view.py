from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm
from webapp.models import Mission
from django.views import View
from django.views.generic import ListView,CreateView
from django.urls import reverse
from .base_view import DetailView, DeleteView, UpdateView


class IndexView(ListView):
    template_name = 'mission/index.html'
    context_object_name = 'missions'
    model = Mission
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Mission.objects.all().order_by('-created_at')

class MissionView(DetailView):
    template_name = 'mission/mission.html'
    model = Mission
    context_key = 'mission'
    context_object= 'mission'



class MissionCreateView(CreateView):
    template_name = 'mission/create.html'
    model = Mission
    form_class = MissionForm


    def get_success_url(self):
        return reverse('mission_view', kwargs={'pk': self.object.pk})


class MissionUpdateView(UpdateView):
    form = MissionForm
    template = 'mission/update.html'
    model = Mission
    context_key = 'mission'
    context_object = 'mission'
    context_form = 'form'
    redirect_url = 'mission_view'

class MissionDeleteView(DeleteView):
    model = Mission
    template = 'mission/delete.html'
    redirect_url = 'index'
    context_object =  'mission'
    context_key = 'mission'
    confirm_deletion = True
