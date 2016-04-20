from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import ListView,CreateView,UpdateView
from models import *
from django.contrib import messages

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

def DeleteCategoryView(request,id):
    try:
        tag=Tag.objects.get(id=id)
        tag.active=0
        tag.save()
        return HttpResponse("success")
    except:
        return HttpResponse("error")
def DeleteQuestionView(request,id):
    try:
        question=QuestionManager.objects.get(id=id)
        question.active=0
        question.save()
        return HttpResponse("success")
    except:
        return HttpResponse("error")

class QuestionView(ListView):
    model = QuestionManager
    context_object_name = 'questionbank'
    template_name="questionmanager/index.html"
    def get_queryset(self):
        questype=self.request.GET.get('questype')
        usertype=self.request.GET.get('usertype')
        questionlist=QuestionManager.objects.filter(active=1, added_by=self.request.user)
        if questype:
            questionlist=questionlist.filter(questype=questype)
        if usertype:
            questionlist=questionlist.filter(usertype=usertype)

        return questionlist
    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['questype'] = Questype
        context['usercat'] = Tag.objects.filter(active=1, added_by=self.request.user)
        return context
class CategoryCreateView(CreateView):
    model = Tag
    #context_object_name = 'tag'
    fields = ['name']
    template_name = "questionmanager/add-categories.html"
    success_url = "/"
    def form_valid(self, form):
        tag_obj=Tag.objects.filter(name=self.request.POST.get('name'),added_by=self.request.user)
        if tag_obj:
            if not tag_obj[0].active:
                tag_obj[0].active=1
                tag_obj[0].save()
                return HttpResponseRedirect("/")
            else:
                return self.form_invalid(form)
        form.instance.added_by = self.request.user
        form.instance.active = 1
        return super(CategoryCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Category Already exist")
        return self.render_to_response({'name':self.request.POST.get('name')}
            )

class CategoryUpdateView(UpdateView):
    model = Tag
    template_name = "questionmanager/update-categories.html"
    context_object_name = 'tag'
    fields = ['name']
    success_url = "/"





