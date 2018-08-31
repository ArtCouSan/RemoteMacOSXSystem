from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', { "template_name" : "login.html"  },  name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^home/$', 'perfis.views.home', name='home')
)


