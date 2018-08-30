from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.login', name='login'),
    url(r'^home/(?P<user_id>\d+)$', 'perfis.views.home', name='home'),
    url(r'^computerEdit/(?P<computer_id>\d+)$', 'perfis.views.computerEdit', name="computerEdit"),
    url(r'^commandEdit/(?P<command_id>\d+)$', 'perfis.views.commandEdit', name="commandEdit")
)


