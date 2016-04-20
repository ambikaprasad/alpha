from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Examples:
    #url(r'^tutorials/$', 'tutorials', name='tutorials'),
    url(r'^$', views.QuestionView.as_view(), name="home"),
    url(r'^question/delete/(?P<id>[-\d]+)/$', views.DeleteQuestionView, name="deletequestion"),
    url(r'^category/$', views.CategoryView.as_view(), name="category"),
    url(r'^category/delete/(?P<id>[-\d]+)/$', views.DeleteCategoryView, name="deletecategory"),
    url(r'^category/add/$', views.CategoryCreateView.as_view(), name="addcategory"),
    url(r'^category/update/(?P<pk>[-\d]+)/$', views.CategoryUpdateView.as_view(), name="updatecategory"),

    ]

