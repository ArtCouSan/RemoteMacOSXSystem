from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import ComputerViewAdd, ComputerViewEdit

urlpatterns = patterns('',
    url(r'^computerEdit/(?P<computer_id>\d+)$', ComputerViewEdit, name="computerGet"),
    url(r'^computerEdit/)$', ComputerViewEdit, name="computerEdit"),
    url(r'^computerAdd/$', ComputerViewAdd, name='computerAdd')
)