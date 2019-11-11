from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.utils.http import urlencode

from webapp.forms import  ProjectForm,MissionForm,SimpleSearchForm
from webapp.models import Project
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse, reverse_lazy

from webapp.views.base_view import StatisticsMixin


class ProjectIndexView(ListView,StatisticsMixin):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(data=self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None



class ProjectView(DetailView,StatisticsMixin):
    template_name = 'project/project.html'
    model = Project

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        context['form'] = ProjectForm()
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


class ProjectCreateView(CreateView,StatisticsMixin):

    template_name = 'project/create.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(UpdateView,StatisticsMixin):
    form_class = ProjectForm
    template_name = 'project/update.html'
    model = Project
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView,StatisticsMixin):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('webapp:project')
    context_object_name =  'project'

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        return super().get(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)