from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView
from models import *

class CategoryView(ListView):
    model = Tag
    context_object_name = 'category'
    template_name="questionmanager/categories.html"
    def get_queryset(self):
        return Tag.category_managaer.filter(active=1, added_by=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['tag'] = Tag.tag_manager.filter(active=1, added_by=self.request.user)
        return context


