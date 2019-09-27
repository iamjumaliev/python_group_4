from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm, StatusForm, TypeForm
from webapp.models import Mission, Status, Type
from django.views import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['missions'] = Mission.objects.all()
        return context

class MissionView(TemplateView):
    template_name = 'mission.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['mission'] = get_object_or_404(Mission, pk=pk)
        return context

class MissionCreateView(View):
    def get(self, request, *args, **kwargs):
        form = MissionForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = MissionForm(data=request.POST)
        if form.is_valid():
            mission = Mission.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('mission_view', pk=mission.pk)
        else:
            return render(request, 'create.html', context={'form': form})


def mission_update_view(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        form = MissionForm(data={
            'summary': mission.summary,
            'description': mission.description,
            'status': mission.status,
            'type': mission.type
        })
        return render(request, 'update.html', context={'form': form, 'mission': mission})
    elif request.method == 'POST':
        form = MissionForm(data=request.POST)
        if form.is_valid():
            mission.summary = form.cleaned_data['summary']
            mission.description = form.cleaned_data['description']
            mission.status = form.cleaned_data['status']
            mission.type = form.cleaned_data['type']
            mission.save()
            return redirect('mission_view', pk=mission.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'mission': mission})


def mission_delete_view(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'mission': mission})
    elif request.method == 'POST':
        mission.delete()
        return redirect('index')


class StatusView(TemplateView):
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context

class Status_View(TemplateView):
    template_name = 'status_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['status'] = get_object_or_404(Status, pk=pk)
        return context

class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'create_status.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'create_status.html', context={'form': form})


def status_update_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'update_status.html', context={'form': form, 'status': status})
    elif request.method == 'POST':
        form = MissionForm(data=request.POST)
        if form.is_valid():
            status.status = form.cleaned_data['status']
            status.save()
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'status_view.html', context={'form': form, 'status': status})


def status_delete_view(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'status_delete.html', context={'status': status})
    elif request.method == 'POST':
        status.delete()
        return redirect('index')



class TypeView(TemplateView):
    template_name = 'type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        return context


class Type_View(TemplateView):
    template_name = 'type_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['type'] = get_object_or_404(Type, pk=pk)
        return context

class TypeCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'create_type.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type = Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type_view.html', context={'form': form})


def type_update_view(request, pk):
    type = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={
            'status': type.type
        })
        return render(request, 'update_type.html', context={'form': form, 'type': type})
    elif request.method == 'POST':
        form = MissionForm(data=request.POST)
        if form.is_valid():
            type.status = form.cleaned_data['type']
            type.save()
            return redirect('type_view', pk=type.pk)
        else:
            return render(request, 'type_view.html', context={'form': form, 'type': type})


def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'type_delete.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type')

# Create your views here.
