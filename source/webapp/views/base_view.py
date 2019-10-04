from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


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