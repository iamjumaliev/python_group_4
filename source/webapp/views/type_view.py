from django.urls import reverse
from webapp.forms import  TypeForm
from webapp.models import  Type
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .base_view import DetailView


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
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})

class TypeUpdateView(UpdateView):
    form_class = TypeForm
    template_name = 'type/update.html'
    model = Type
    context_key = 'type'
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('type_view', kwargs={'pk': self.object.pk})

class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/delete.html'
    success_url = 'type/type.html'
    context_object_name =  'type'

