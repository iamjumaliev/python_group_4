from accounts.forms import UserChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from .forms import UserCreationForm, UserChangePasswordForm


def login_view(request):
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


def logout_view(request):
    logout(request)
    return redirect('webapp:login')

def register_view(request, *args, **kwargs):
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

class UserChangeView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserChangeForm

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserChangePasswordView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_change_password.html'
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:login')


class UsersList(ListView):
    template_name = 'users_list.html'
    context_object_name = 'users'
    model = User
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return User.objects.all()


# Create your views here.
