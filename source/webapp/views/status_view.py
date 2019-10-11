from django.urls import reverse
from webapp.forms import  StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView,DeleteView
from .base_view import DetailView, UpdateView


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
    template_name = 'status/create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView):
    form = StatusForm
    template = 'status/update.html'
    model = Status
    context_key = 'status'
    context_object = 'status'
    context_form = 'form'
    redirect_url = 'status_view'

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = 'status/status.html'
    context_object_name =  'status'
