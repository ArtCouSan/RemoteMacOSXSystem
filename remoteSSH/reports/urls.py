from django.urls import path
from django.contrib import admin
from reports.views import ReportsView
from . import views

urlpatterns = [
    # List reports
    path('report/',  ReportsView.as_view(), name="report")
]