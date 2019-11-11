# from django.http import request
# from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()


class DetailView(TemplateView):
    model = None
    context_object = None
    context_key = 'objects'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        self.context_object = get_object_or_404(self.model, pk=pk)
        context[self.context_key] = self.context_object
        return context


class DeleteView(View):
    model = None
    template = ''
    redirect_url = ''
    context_key = 'object'
    confirm_deletion = True





    def get(self,  *args, **kwargs):
        obj = self.get_object()
        if self.confirm_deletion:
            return render(self.request, self.template,context={self.context_key: obj})
        else:
            self.delete_object(obj)
            return redirect(self.get_redirect_url())



    def post(self, *args, **kwargs):
        obj = self.get_object()
        self.delete_object(obj)
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(self.model, pk=pk)
        return obj

    def delete_object(self, obj):
        return obj.delete()




class UpdateView(View):
    form = None
    template = ''
    model = None
    context_key = 'object'
    context_object = None
    context_form = None
    redirect_url = ''


    def get(self,request,*args, **kwargs):
        obj = self.get_object()
        form = self.form(instance=obj)
        return render(request, self.template, context={self.context_form: form, self.context_object: obj})

    def post(self,*args, **kwargs):
        obj = self.get_object()
        form = self.form(data=self.request.POST,instance=obj)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(self.request)

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(self.model, pk=pk)
        return obj

    def form_valid(self, form):
        obj = self.get_object()
        form.save()
        return redirect(self.get_redirect_url(), pk=obj.pk)

    def form_invalid(self, *args, **kwargs):
        obj = self.get_object()
        form = self.form
        return render(self.request, self.template, context={self.context_form: form, self.context_object: obj})

    def get_redirect_url(self):
        return self.redirect_url


class StatisticsMixin:
    stat = {}
    total_counter = 0

    def set_request(self, request):
        self.request = request

    def save_in_session(self):
        self.request.session['session_stat'] = self.stat

    def page_login(self):
        self.session_counter()

    def session_counter(self):
        if self.request.path not in self.stat.keys():
            self.stat[self.request.path] = 1
        elif self.request.path in self.stat.keys():
            self.stat[self.request.path] += 1

    def clean_dict_data(self):
        data = {}
        for key, value in self.request.session['session_stat'].items():
            if key == '/':
                data['main_page'] = value
            elif key != '/':
                data[key.replace('/', '')] = value
        print(data)
        return data

    # def time_counter(self):
    #     pass
