from django.shortcuts import render, redirect
from computer.models import Computer
from django.views.generic.base import View
from computer.forms import ComputerForm
from django.contrib.auth.decorators import login_required

def computerRemove(req, computer_id):
    computer = Computer.objects.filter(id = computer_id).delete()
    return redirect('home')

class ComputerViewEdit(View):

    template_name = 'pagina_computer.html'

    
    def get(self, req, computer_id):
        computer = Computer.objects.get(id = computer_id)
        return render(req, self.template_name,  {"computer": computer })
    
   
    def post(self, req, computer_id):

        form = ComputerForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            Computer.objects.filter(id = computer_id).update(name = dados_form['name'],ip = dados_form['ip'],userLogin =  dados_form['userLogin'],user =  dados_form['user'],password =  dados_form['password'])
            return redirect('home')

        return render(req, self.template_name, {'form' : form })

class ComputerViewAdd(View):

    template_name = 'pagina_computer.html'

    
    def get(self, req):
        return render(req, self.template_name)
    
    
    def post(self, req):

        form = ComputerForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            computer = Computer.objects.create(name = dados_form['name'],ip =  dados_form['ip'],userLogin =  dados_form['userLogin'],user = dados_form['user'], password = dados_form['password'])
            computer.save()
            return redirect('home')

        return render(req, self.template_name, {'form' : form })