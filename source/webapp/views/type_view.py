from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import  TypeForm
from webapp.models import  Type
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView

from webapp.views.base_view import StatisticsMixin


class TypeIndexView(ListView,StatisticsMixin):
    template_name = 'type/type.html'
    context_object_name = 'types'
    model = Type
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Type.objects.all()



class TypeView(DetailView,StatisticsMixin):

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    template_name = 'type/type_view.html'
    model = Type
    context_object_name = 'type'

class TypeCreateView(CreateView,StatisticsMixin):

    template_name = 'type/create.html'
    model = Type
    form_class = TypeForm
    context_object_name = 'type'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:type_view', kwargs={'pk': self.object.pk})

class TypeUpdateView(UpdateView):
    form_class = TypeForm
    template_name = 'type/update.html'
    model = Type
    context_object_name = 'type'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:type_view', kwargs={'pk': self.object.pk})

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/delete.html'
    success_url = reverse_lazy('webapp:type')
    context_object_name =  'type'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

