from webapp.forms import MissionForm
from webapp.models import Mission
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse, reverse_lazy



class IndexView(ListView):
    template_name = 'mission/index.html'
    context_object_name = 'missions'
    model = Mission
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Mission.objects.all().order_by('-created_at')

class MissionView(DetailView):
    template_name = 'mission/mission.html'
    model = Mission
    context_object_name = 'mission'



class MissionCreateView(CreateView):
    template_name = 'mission/create.html'
    model = Mission
    form_class = MissionForm


    def get_success_url(self):
        return reverse('mission_view', kwargs={'pk': self.object.pk})


class MissionUpdateView(UpdateView):
    form_class = MissionForm
    template_name = 'mission/update.html'
    model = Mission
    context_object_name = 'mission'

    def get_success_url(self):
        return reverse('mission_view', kwargs={'pk': self.object.pk})

class MissionDeleteView(DeleteView):
    model = Mission
    template_name = 'mission/delete.html'
    success_url = reverse_lazy('index')
    context_object_name =  'mission'

