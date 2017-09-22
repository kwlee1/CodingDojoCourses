from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^create',views.create),
    url(r'^destroy/(?P<id>[0-9]{1,})$', views.destroy), 
    url(r'^delete/(?P<id>[0-9]{1,})$', views.delete), 
]