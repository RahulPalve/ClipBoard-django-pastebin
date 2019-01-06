from django.conf.urls import url
from todoapp import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<td_no>[-\w]+)/$', views.show_todo, name='show_todo'),
]