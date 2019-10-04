from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm, StatusForm, TypeForm
from webapp.models import Mission, Type
from django.views import View
from django.views.generic import ListView
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

class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type/type_view.html', context={'form': form})


def type_update_view(request, pk):
    type = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'status': type.type
        })
        return render(request, 'type/update_type.html', context={'form': form, 'type': type})
    elif request.method == 'POST':
        form = MissionForm(data=request.POST)
        if form.is_valid():
            type.status = form.cleaned_data['type']
            type.save()
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type/type_view.html', context={'form': form, 'type': type})


def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'type/type_delete.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type')
