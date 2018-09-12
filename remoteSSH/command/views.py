from django.shortcuts import render, redirect
from command.models import Command
from computer.models import Computer
from django.views.generic import View
from command.forms import CommandForm
from django.contrib.auth.decorators import login_required

# Remover commando pelo id
def commandRemove(req, command_id):
    command = Command.objects.filter(id = command_id).delete()

     # Valores para tabela na pagina principal
    commands = Command.objects.all()
    computers = Computer.objects.all()

    return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Comando excluido com sucesso."})

# Edicao e apresentacao de page edit
class CommandViewEdit(View):

    template_name = 'pagina_command.html'

    # Retorna pagina de edicao com comando buscado
    def get(self, req, command_id):
        command = Command.objects.get(id = command_id)
        return render(req, self.template_name,  {"command": command })
    
    # Atualiza no banco o comando com validacao
    def post(self, req, command_id):

        form = CommandForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            cm = Command.objects.get(id = command_id)
            cm.category = dados_form['category']
            cm.name = dados_form['name']
            cm.command = dados_form['command']
            cm.save()

            
            # Valores para tabela na pagina principal
            commands = Command.objects.all()
            computers = Computer.objects.all()

            return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Comando editado com sucesso."})

        return render(req, self.template_name, {'form' : form })

# Adiciona comando
class CommandViewAdd(View):

    template_name = 'pagina_command.html'

    # Retorna pagina para adicao de comando
    def get(self, req):
        return render(req, self.template_name)
    
    # Adiciona comando
    def post(self, req):

        form = CommandForm(req.POST)

        # Verifica validacao
        if form.is_valid():
            dados_form = form.data
            command = Command.objects.create(category = dados_form['category'],name = dados_form['name'],command = dados_form['command'])
            command.save()
            
            # Valores para tabela na pagina principal
            commands = Command.objects.all()
            computers = Computer.objects.all()

            return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Comando editado com sucesso."})


        return render(req, self.template_name, {'form' : form })