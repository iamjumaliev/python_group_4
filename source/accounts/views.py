from accounts.forms import UserChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from accounts.models import UserProfile
from .forms import UserCreationForm, UserChangePasswordForm
from webapp.views.base_view import StatisticsMixin


def login_view(request,StatisticsMixin):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context=context)

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context


def logout_view(request,StatisticsMixin):
    logout(request)

    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context
    return redirect('webapp:login')

def register_view(request,StatisticsMixin, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        self.set_request(request=request)
        self.page_login()
        self.save_in_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.clean_dict_data()
        return context

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'



class UserChangeView(UserPassesTestMixin,StatisticsMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserChangeForm

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
        return self.get_object() == self.request.user


    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})



class UserChangePasswordView(StatisticsMixin,UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_change_password.html'
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

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
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:login')


class UsersList(ListView):
    template_name = 'users_list.html'
    context_object_name = 'users'
    model = User
    paginate_by = 3
    paginate_orphans = 1




# Create your views here.
