from django.shortcuts import render, redirect
from command.models import Command
from django.views.generic import View
from command.forms import CommandForm
from django.contrib.auth.decorators import login_required

def commandRemove(req, command_id):
    command = Command.objects.filter(id = command_id).delete()
    return redirect('home')

class CommandViewEdit(View):

    template_name = 'pagina_command.html'

    def get(self, req, command_id):
        command = Command.objects.get(id = command_id)
        return render(req, self.template_name,  {"command": command })
    
    def post(self, req, command_id):

        form = CommandForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            Command.objects.filter(id = command_id).update(category = dados_form['category'],name = dados_form['name'],command =  dados_form['command'])
            return redirect('home')

        return render(req, self.template_name, {'form' : form })

class CommandViewAdd(View):

    template_name = 'pagina_command.html'

    def get(self, req):
        return render(req, self.template_name)
    
    def post(self, req):

        form = CommandForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            command = Command.objects.create(category = dados_form['category'],name = dados_form['name'],command = dados_form['command'])
            command.save()
            return redirect('home')

        return render(req, self.template_name, {'form' : form })