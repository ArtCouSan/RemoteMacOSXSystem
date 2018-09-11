from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from command.models import Command
from computer.models import Computer
from django.contrib.auth.decorators import login_required
from perfis.ssh import *
from perfis.models import Result
import paramiko
import sys

class ReportsView(TemplateView):
 
    template_name = 'pagina_relatorios.html'

    def get(self, req):

        # Valores para tabela na pagina principal
        commands = Command.objects.filter(report = 1)
        computers = Computer.objects.all()

        # Verifica e muda os status dos computadores
        verifyConnection(computers)

        return render(req, self.template_name, { "computers": computers,"commands": commands})

    def post(self, req):
        
        # Valores para tabela na pagina principal 
        commands = Command.objects.filter(report = 1)
        computers = Computer.objects.all()

        # Deleta comandos da ultima requisicao
        Result.objects.all().delete()

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
                    
                    # Testa conexao
                    try:

                        # Cria conexao com a maquina             
                        client.connect(hostname, "22", user, password, timeout = 3)

                        # Verifica comando
                        try:

                            # Executa comando 
                            stdin, stdout, stderr = client.exec_command(command)
                        
                            # Verifica saida
                            if stdout.channel.recv_exit_status() == 0:

                                # Salva resultado
                                strReport = 'Maquina {} com comando ( {} ) habilitado'.format(cp.ip, cm.name)
            
                                
                        # Erro de comando
                        except:

                            # Salva resultado
                            strReport = 'Sem acesso a maquina {} para validar o comando: {} (Comando invalido ou falha de permissão)'.format(cp.ip, cm.name)
            
                        # Encerra conexaos
                        client.close()

                    # Erro de conexao
                    except:

                        # Salva resultado
                        strReport = 'Sem acesso a maquina {} para validar o comando: {} (Falha de conexão)'.format(cp.ip, cm.name)
                             
            return redirect("report")
            
        else:
            
            return render(req, self.template_name, { "computers": computers,"commands": commands})