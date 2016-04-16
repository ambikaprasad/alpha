from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    #url(r'^tutorials/$', 'tutorials', name='tutorials'),
    url(r'^$', TemplateView.as_view(template_name='questionmanager/index.html'), name="home"),
    url(r'^category/$', TemplateView.as_view(template_name='questionmanager/categories.html'), name="category"),
    ]

