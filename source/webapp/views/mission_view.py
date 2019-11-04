from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.utils.http import urlencode

from webapp.forms import MissionForm,SimpleSearchForm
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


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
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

class MissionView(DetailView):
    template_name = 'mission/mission.html'
    model = Mission
    context_object_name = 'mission'



class MissionCreateView(CreateView,UserPassesTestMixin):
    template_name = 'mission/create.html'
    model = Mission
    form_class = MissionForm

    def test_func(self):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(self.request, self.args, self.kwargs)
        # else:
        #     self.


    def get_success_url(self):
        return reverse('webapp:mission_view', kwargs={'pk': self.object.pk})


class MissionUpdateView(UserPassesTestMixin,UpdateView):
    form_class = MissionForm
    template_name = 'mission/update.html'
    model = Mission
    context_object_name = 'mission'

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        project = self.get_object().project
        print(project.team_project)
        user =  self.request.user

        #
        # if user == project.project.user:
        #     print(project.project.user)
        return True



    def get_success_url(self):
        return reverse('webapp:mission_view', kwargs={'pk': self.object.pk})

class MissionDeleteView(DeleteView):
    model = Mission
    template_name = 'mission/delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name =  'mission'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


