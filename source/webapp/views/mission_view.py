from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm
from webapp.models import Mission
from django.views import View
from django.views.generic import TemplateView, ListView


class IndexView(ListView):
    template_name = 'mission/index.html'
    context_object_name = 'missions'
    model = Mission
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Mission.objects.all().order_by('-created_at')

class MissionView(TemplateView):
    template_name = 'mission/mission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        mission = get_object_or_404(Mission, pk=pk)
        context['mission'] = mission
        context['form'] = MissionForm()
        return context


class MissionCreateView(View):
    def get(self, request, *args, **kwargs):
        form = MissionForm()
        return render(request, 'mission/create.html', context={'form': form})

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
            return render(request, 'mission/create.html', context={'form': form})


def MissionUpdateView(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        form = MissionForm(data={
            'summary': mission.summary,
            'description': mission.description,
            'status': mission.status,
            'type': mission.type
        })
        return render(request, 'mission/update.html', context={'form': form, 'mission': mission})
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
            return render(request, 'mission/update.html', context={'form': form, 'mission': mission})


def MissionDeleteView(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'GET':
        return render(request, 'mission/delete.html', context={'mission': mission})
    elif request.method == 'POST':
        mission.delete()
        return redirect('index')
