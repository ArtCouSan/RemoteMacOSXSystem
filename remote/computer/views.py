from django.shortcuts import render, redirect
from computer.models import *
from django.views.generic import View
from computer.forms import ComputerForm
from django.contrib.auth.models import Computer

class ComputerViewEdit(View):

    template_name = 'pagina_computer.html'

    def get(self, req, computer_id):
        computer = Computer.objects.get(id = computer_id)
        return render(request, self.template_name,  {"computer": computer })
    
    def post(self, req, , computer_id):

        form = ComputerForm(req.Post)

        if form.is_valid():
            dados_form = form.data
            computer.objects.get(id = computer_id).update(name = dados_form['name'],ip = dados_form['ip'],userLogin =  dados_form['userLogin'],user =  dados_form['user'],password =  dados_form['password'])
            computer.save()
            return redirect('home')


        return render(request, self.template_name, {'form' : form })


class ComputerViewAdd(View):

    template_name = 'pagina_computer.html'

    def get(self, req):
        return render(request, self.template_name)
    
    def post(self, req):

        form = ComputerForm(req.Post)

        if form.is_valid():
            dados_form = form.data
            computer = Computer.objects.create_computer(dados_form['name'], dados_form['ip'], dados_form['userLogin'], dados_form['user'], dados_form['password'])
            computer.save()
            return redirect('home')


        return render(request, self.template_name, {'form' : form })