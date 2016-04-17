from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Examples:
    #url(r'^tutorials/$', 'tutorials', name='tutorials'),
    url(r'^$', views.QuestionView.as_view(), name="home"),
    url(r'^category/$', views.CategoryView.as_view(), name="category"),
    url(r'^category/delete/(?P<tag>[-\d]+)/$', views.DeleteCategoryView, name="deletecategory"),
    ]

