from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import ComputerViewAdd, ComputerViewEdit

urlpatterns = patterns('',
    url(r'^computerEdit/(?P<computer_id>\d+)$', ComputerViewEdit.as_view(), name="computerEdit"),
    url(r'^computerAdd/$', ComputerViewAdd.as_view(), name='computerAdd'),
    url(r'^computerRemove/(?P<computer_id>\d+)$', 'computer.views.computerRemove', name='computerRemove')
)