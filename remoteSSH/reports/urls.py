from django.urls import path
from django.contrib import admin
from reports.views import ReportsView
from . import views
from reports.views import ReportViewEdit, ReportViewAdd

urlpatterns = [
    # List reports
    path('report/',  ReportsView.as_view(), name="report"),
    # Edit Report
    path('reportEdit/<int:report_id>', ReportViewEdit.as_view(), name="reportEdit"),
    # Add Report
    path('reportAdd/', ReportViewAdd.as_view(), name='reportAdd'),
    # Remove Report
    path('reportRemove/<int:report_id>', views.reportRemove, name='reportRemove')
]