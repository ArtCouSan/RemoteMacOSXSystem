from django.shortcuts import render, redirect
from computer.models import Computer
from django.views.generic.base import View
from computer.forms import ComputerForm
from django.contrib.auth.decorators import login_required

# Remover computador pelo id
def computerRemove(req, computer_id):
    computer = Computer.objects.filter(id = computer_id).delete()
    return redirect('home')

# Edicao e apresentacao de page edit
class ComputerViewEdit(View):

    template_name = 'pagina_computer.html'

    # Retorna pagina de edicao com computer buscado
    def get(self, req, computer_id):
        computer = Computer.objects.get(id = computer_id)
        return render(req, self.template_name,  {"computer": computer })

    # Atualiza no banco o computador com validacao
    def post(self, req, computer_id):

        form = ComputerForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            cp = Computer.objects.get(id = computer_id)
            cp.name = dados_form['name']
            cp.ip = dados_form['ip']
            cp.userLogin =  dados_form['userLogin']
            cp.user =  dados_form['user']
            cp.password =  dados_form['password']
            cp.save()
            return redirect('home')

        return render(req, self.template_name, {'form' : form })

# Adiciona computador
class ComputerViewAdd(View):

    template_name = 'pagina_computer.html'

    # Retorna pagina para adicao de computador
    def get(self, req):
        return render(req, self.template_name)
    
    # Adiciona computador
    def post(self, req):

        form = ComputerForm(req.POST)

        # Verifica validacao
        if form.is_valid():
            dados_form = form.data
            computer = Computer.objects.create(name = dados_form['name'],ip =  dados_form['ip'],userLogin =  dados_form['userLogin'],user = dados_form['user'], password = dados_form['password'])
            computer.save()
            return redirect('home')

        return render(req, self.template_name, {'form' : form })