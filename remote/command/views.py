from django.shortcuts import render, redirect
from command.models import *
from django.views.generic import View
from command.forms import CommandForm
from django.contrib.auth.models import Command


class CommandEditView(View):

    template_name = 'pagina_command.html'

    def get(self, req, command_id):
        command = Command.objects.get(id = command_id)
        return render(request, self.template_name,  {"command": command })
    
    def post(self, req, , command_id):

        form = CommandForm(req.Post)

        if form.is_valid():
            dados_form = form.data
            command.objects.get(id = command_id).update(category = dados_form['category'],name = dados_form['name'],command =  dados_form['command'])
            command.save()
            return redirect('home')

        return render(request, self.template_name, {'form' : form })


class CommandAddView(View):

    template_name = 'pagina_command.html'

    def get(self, req):
        return render(request, self.template_name)
    
    def post(self, req):

        form = CommandForm(req.Post)

        if form.is_valid():
            dados_form = form.data
            command = Command.objects.create_command(dados_form['category'],dados_form['name'],dados_form['command'])
            computer.save()
            return redirect('home')


        return render(request, self.template_name, {'form' : form })