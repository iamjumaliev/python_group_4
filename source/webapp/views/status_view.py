from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import  StatusForm
from webapp.models import Status
from django.views.generic import ListView, CreateView,DeleteView,UpdateView,DetailView

from webapp.views.base_view import StatisticsMixin


class StatusIndexView(ListView,StatisticsMixin):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.clean_dict_data()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Status.objects.all()


class StatusView(DetailView,StatisticsMixin):

    template_name = 'status/status_view.html'
    model = Status
    context_object_name = 'status'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.clean_dict_data()
        return super().get(request, *args, **kwargs)


class StatusCreateView(CreateView, StatisticsMixin):
    template_name = 'status/create.html'
    model = Status
    form_class = StatusForm

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.clean_dict_data()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})


class StatusUpdateView(UpdateView,StatisticsMixin):
    form_class = StatusForm
    template_name = 'status/update.html'
    model = Status
    context_object_name = 'status'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.clean_dict_data()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:status_view', kwargs={'pk': self.object.pk})

class StatusDeleteView(DeleteView,StatisticsMixin):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('webapp:status')
    context_object_name =  'status'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.clean_dict_data()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
