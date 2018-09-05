from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class ReportsView(TemplateView):
 
    template_name = 'pagina_reports.html'

    def get(self, req):
        pass

    def post(self, req):
        pass