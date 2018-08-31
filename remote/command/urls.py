from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import CommandViewEdit, CommandViewAdd

urlpatterns = patterns('',
    url(r'^commandEdit/(?P<command_id>\d+)$', CommandViewEdit.as_view(), name="commandEdit"),
    url(r'^commandAdd/$', CommandViewAdd.as_view(), name='commandAdd'),
    url(r'^commandRemove/(?P<command_id>\d+)$', 'command.views.commandRemove', name='commandRemove')

)

