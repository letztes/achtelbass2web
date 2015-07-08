from django.conf.urls import patterns, url

from generate_notes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
