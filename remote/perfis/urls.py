from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.login'),
    url(r'^home/(?P<user_id>\d+)$', 'perfis.views.home')
)


