from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import CommandViewEdit, CommandViewAdd

urlpatterns = patterns('',
    url(r'^commandEdit/(?P<command_id>\d+)$', CommandViewEdit, name="commandEdit"),
    url(r'^commandEdit/)$', CommandViewEdit, name="commandEdit"),
    url(r'^commandAdd/$', CommandViewAdd, name='commandAdd')
)

