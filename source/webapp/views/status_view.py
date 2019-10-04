from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import MissionForm, StatusForm
from webapp.models import Status
from django.views import View
from django.views.generic import TemplateView,ListView

class StatusIndexView(ListView):
    template_name = 'status/status.html'
    context_object_name = 'statuses'
    model = Status
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Status.objects.all()


class StatusView(TemplateView):
    template_name = 'status/status_view.html'

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['status'] = get_object_or_404(Status, pk=pk)
        return context

class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/create_status.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status = Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_view', pk=status.pk)
        else:
            return render(request, 'status/create_status.html', context={'form': form})


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
