from django.conf.urls import url
from todoapp import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<link_c>[-\w]+)/$', views.show_todo, name='show_todo'),
    url(r'^all/$', views.all, name='all'),
]