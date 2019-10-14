from django.core.paginator import Paginator

from webapp.forms import  ProjectForm,MissionForm
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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['form'] = MissionForm()
        missions = project.mission_project.order_by('-created_at')
        self.paginate_mission_project_to_context(missions, context)
        return context

    def paginate_mission_project_to_context(self, missions, context):
        paginator = Paginator(missions, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['missions'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ProjectCreateView(CreateView):

    template_name = 'project/create.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project')
    context_object_name =  'project'