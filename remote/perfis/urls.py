from django.conf.urls import patterns, include, url
from django.contrib import admin
from perfis import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^home/(?P<user_id>\d+)$', views.home, name='home')
)


