from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import  StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,DetailView



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
    context_object_name = 'status'


class StatusCreateView(CreateView):
    template_name = 'status/create.html'
    model = Status
    form_class = StatusForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView):
    form_class = StatusForm
    template_name = 'status/update.html'
    model = Status
    context_object_name = 'status'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('webapp:status')
    context_object_name =  'status'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
