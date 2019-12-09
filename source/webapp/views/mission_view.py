from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.template import context
from django.utils.http import urlencode
from django.views.generic.edit import FormMixin

from webapp.forms import MissionForm,SimpleSearchForm
from webapp.models import Mission, Team, Project
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy

from webapp.views.base_view import StatisticsMixin


class IndexView(StatisticsMixin,ListView):
    template_name = 'mission/index.html'
    context_object_name = 'missions'
    model = Mission
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)




    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(summary__icontains=self.search_value)
                | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['stats'] = self.clean_dict_data()
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

class MissionView(StatisticsMixin,DetailView):
    template_name = 'mission/mission.html'
    model = Mission
    context_object_name = 'mission'
    #
    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        # self.stat.clear()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context





class MissionCreateView(PermissionRequiredMixin,CreateView,StatisticsMixin):
    template_name = 'mission/create.html'
    model = Mission
    form_class = MissionForm
    permission_required = 'webapp.add_mission'
    permission_denied_message = "Доступ запрещён"


    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        project = self.get_object().project
        users_project = Project.objects.filter(
            team_project__user=self.request.user)
        if project not in users_project:
            return False
        return True



    def get_success_url(self):
        return reverse('webapp:mission_view', kwargs={'pk': self.object.pk})


class MissionUpdateView(PermissionRequiredMixin,UserPassesTestMixin,UpdateView,StatisticsMixin):
    form_class = MissionForm
    template_name = 'mission/update.html'
    model = Mission
    context_object_name = 'mission'
    permission_required = 'webapp.update_mission'
    permission_denied_message = "Доступ запрещён"

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context


    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        project = self.get_object().project
        users_project = Project.objects.filter(
            team_project__user=self.request.user)
        if project not in users_project:
            return False
        return True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['project'] = self.object.project
        return kwargs

    def get_success_url(self):
        return reverse('webapp:mission_view', kwargs={'pk': self.object.pk})

class MissionDeleteView(PermissionRequiredMixin,DeleteView,UserPassesTestMixin,StatisticsMixin):
    model = Mission
    template_name = 'mission/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name =  'mission'
    permission_required = 'webapp.delete_mission'
    permission_denied_message = "Доступ запрещён"

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        project = self.get_object().project
        users_project = Project.objects.filter(
            team_project__user=self.request.user)
        if project not in users_project:
            return False
        return True

