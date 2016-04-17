from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView
from models import *

class CategoryView(ListView):
    model = Tag
    context_object_name = 'tag'
    template_name="questionmanager/categories.html"
    #queryset = Tag.objects.filter(active=1, added_by=self.request.user)
    def get_queryset(self):
        return Tag.objects.filter(active=1, added_by=self.request.user)
    '''def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['tag'] = Tag.tag_manager.filter(active=1, added_by=self.request.user)
        return context'''

def DeleteCategoryView(request,tag):
    try:
        tag=Tag.objects.get(id=tag)
        tag.active=0
        tag.save()
        return HttpResponse("success")
    except:
        return HttpResponse("success")

class QuestionView(ListView):
    model = QuestionManager
    context_object_name = 'questionbank'
    template_name="questionmanager/index.html"
    def get_queryset(self):
        return QuestionManager.objects.filter(active=1, added_by=self.request.user)






