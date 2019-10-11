from webapp.forms import MissionForm
from webapp.models import Project
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse, reverse_lazy



class ProjectIndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Project.objects.all().order_by('created_at')



class ProjectView(DetailView):
    template_name = 'project/project.html'
    model = Project
    context_object_name = 'project'





class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project/index')
    context_object_name =  'project'