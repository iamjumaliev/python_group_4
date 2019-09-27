from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm
from webapp.models import Mission
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
# Create your views here.
