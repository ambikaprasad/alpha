from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Examples:
    #url(r'^tutorials/$', 'tutorials', name='tutorials'),
    url(r'^$', TemplateView.as_view(template_name='questionmanager/index.html'), name="home"),
    url(r'^category/$', views.CategoryView.as_view(), name="category"),
    ]

