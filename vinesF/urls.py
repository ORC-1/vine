'''
Created on 26 Nov 2017

@author: ORC-1
'''
from django.conf.urls import include, url
from django.contrib import admin
from vinesF import views
import vinesF

#Generic View System
app_name ='vinesF'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.latest, name='latest'),
    url(r'^lt$',views.Mol, name='Mol'),
    #url(r'^NewVid/$',views.NewVid, name='NewVid'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^detail/', views.DetailView.as_view(), name='detail'),
    
    
]