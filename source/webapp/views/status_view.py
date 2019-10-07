from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import MissionForm, StatusForm
from webapp.models import Status
from django.views import View
from django.views.generic import ListView, CreateView
from .base_view import DetailView


class StatusIndexView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Status.objects.all()


class StatusView(DetailView):

    template_name = 'status/status_view.html'
    model = Status
    context_object = 'status'
    context_key = 'status'


class StatusCreateView(CreateView):
    template_name = 'type/create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})


def status_update_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'status/update_status.html', context={'form': form, 'status': status})
    elif request.method == 'POST':
        form = MissionForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['status']
            status.save()
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'status/status_view.html', context={'form': form, 'status': status})


def status_delete_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'status/status_delete.html', context={'status': status})
    elif request.method == 'POST':
        status.delete()
        return redirect('index')
