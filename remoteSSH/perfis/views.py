from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from command.models import Command
from computer.models import Computer
from django.contrib.auth.decorators import login_required
import paramiko
import sys

def login(req):
    return render(req, 'login.html')


class HomeSSHView(TemplateView):

    template_name = 'pagina_principal.html'

    def get(self, req):

        # Valores para tabela na pagina principal
        commands = Command.objects.all()
        computers = Computer.objects.all()

        return render(req, self.template_name, { "computers": computers,"commands": commands})


    def post(self, req):

        # Valores para tabela na pagina principal 
        commands = Command.objects.all()
        computers = Computer.objects.all()

        # Verifica requisicao
        if req.method == 'POST':

            # Arrays para receber computadores do banco
            computersArrays = []
            commandsArrays = []
        
            # Declara variavel com dados da requisicao ajax
            computersIdArrays = req.POST.getlist('computers[]')
            commandsIdArrays = req.POST.getlist('commands[]')

            # Preenche array com computadores buscados no banco
            for cpId in computersIdArrays:
                i = Computer.objects.get(id = cpId)
                computersArrays.append(i)

            # Preenche array com comandos buscados no banco
            for cmId in commandsIdArrays:
                k = Command.objects.get(id = cmId)
                commandsArrays.append(k)

            # Cria variavel com paramiko SSH
            client = paramiko.SSHClient()

            # Loop nos computadores 
            for cp in computersArrays:

                # Loop nos commandos
                for cm in commandsArrays:

                    # Declara atributo da conexao
                    user = str(cp.user)
                    hostname = str(cp.ip)
                    password = str(cp.password)

                    # Declara comando
                    command = str(cm.command)

                    # Carrega as chaves de conexao conhecida do sistema
                    client.load_system_host_keys()
                    client.set_missing_host_key_policy(paramiko.WarningPolicy)  

                    # Cria conexao com a maquina              
                    client.connect(hostname, "22", user, password)

                    # Executa comando
                    stdin, stdout, stderr = client.exec_command(command)

                    # Encerra conexaos
                    client.close()

            return render(req, self.template_name, { "computers": computers,"commands": commands})
            
        else:
            
            return render(req, self.template_name, { "computers": computers,"commands": commands})

