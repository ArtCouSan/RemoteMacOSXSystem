from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from command.models import Command
from computer.models import Computer
from django.contrib.auth.decorators import login_required
from perfis.ssh import *
from perfis.models import Result
from reports.reportLab import geraPdf
from reports.forms import ReportForm
from reports.models import Report
import paramiko
import sys
from reportlab.pdfgen import canvas
from django.views.generic import View

# Exemplo de report [[ 0 -eq $(comando) ]] && echo 1

class ReportsView(TemplateView):
 
    template_name = 'pagina_relatorios.html'

    def get(self, req):

        # Valores para tabela na pagina principal
        reports = Report.objects.all()
        computers = Computer.objects.all()

        # Verifica e muda os status dos computadores
        verifyConnection(computers)

        return render(req, self.template_name, { "computers": computers,"reports": reports})

    def post(self, req):
        
        # Valores para tabela na pagina principal 
        commands = Command.objects.all()
        computers = Computer.objects.all()

        # Array com reports
        reportsArray = []

        # Deleta comandos da ultima requisicao
        Result.objects.all().delete()

        # Verifica requisicao
        if req.method == 'POST':

            # Arrays para receber computadores do banco
            computersArrays = []
            reportsArrays = []

            # Declara variavel com dados da requisicao ajax
            computersIdArrays = req.POST.getlist('computers[]')
            reportsIdArrays = req.POST.getlist('reports[]')

            # Preenche array com computadores buscados no banco
            for cpId in computersIdArrays:
                i = Computer.objects.get(id = cpId)
                computersArrays.append(i)

            # Preenche array com reports buscados no banco
            for rpId in reportsIdArrays:
                k = Report.objects.get(id = rpId)
                reportsArrays.append(k)

            # Cria variavel com paramiko SSH
            client = paramiko.SSHClient()

            # Loop nos computadores 
            for cp in computersArrays:
                
                # Loop nos commandos
                for rp in reportsArrays:

                    # Declara atributo da conexao
                    user = str(cp.user)
                    hostname = str(cp.ip)
                    password = str(cp.password)

                    # Declara comando
                    command = str(rp.command)

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
                            
                            out = stdout.read().decode('ascii').strip("\n")

                            # Verifica saida
                            if out == rp.condition or out is rp.condition:

                                # Salva resultado
                                strReport = 'Maquina {} com comando ( {} ) habilitado'.format(cp.ip, rp.name)

                                reportsArray.append(strReport)
                            
                            else:

                                # Salva resultado
                                strReport = 'Maquina {} com comando ( {} ) desabilitado'.format(cp.ip, rp.name)

                                reportsArray.append(strReport)
                            
                        # Erro de comando
                        except:

                            # Salva resultado
                            strReport = 'Sem acesso a maquina {} para validar o comando: {} (Comando invalido ou falha de permissão)'.format(cp.ip, rp.name)
            
                            reportsArray.append(strReport)

                        # Encerra conexaos
                        client.close()

                    # Erro de conexao
                    except:

                        # Salva resultado
                        strReport = 'Sem acesso a maquina {} para validar o comando: {} (Falha de conexão)'.format(cp.ip, rp.name)

                        reportsArray.append(strReport)

            geraPdf(canvas, reportsArray)
                             
            return redirect("home")
            
        else:
            
            return redirect("home")

# Remover report pelo id
def reportRemove(req, report_id):
    report = Report.objects.filter(id = report_id).delete()

    # Valores para tabela na pagina principal
    commands = Command.objects.all()
    computers = Computer.objects.all()

    return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Report  excluido com sucesso."})

# Edicao e apresentacao de page edit
class ReportViewEdit(View):

    template_name = 'pagina_report.html'

    # Retorna pagina de edicao com comando buscado
    def get(self, req, report_id):
        report = Report.objects.get(id = report_id)
        return render(req, self.template_name,  {"report": report })
    
    # Atualiza no banco o report com validacao
    def post(self, req, report_id):

        form = ReportForm(req.POST)

        if form.is_valid():
            dados_form = form.data
            rp = Report.objects.get(id = report_id)
            rp.condition = dados_form['condition']
            rp.name = dados_form['name']
            rp.command = dados_form['command']
            rp.save()
            
            # Valores para tabela na pagina principal
            commands = Command.objects.all()
            computers = Computer.objects.all()

            return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Report editado com sucesso."})

        return render(req, self.template_name, {'form' : form })

# Adiciona report
class ReportViewAdd(View):

    template_name = 'pagina_report.html'

    # Retorna pagina para adicao de report
    def get(self, req):
        return render(req, self.template_name)
    
    # Adiciona comando
    def post(self, req):

        form = ReportForm(req.POST)

        # Verifica validacao
        if form.is_valid():
            dados_form = form.data
            report = Report.objects.create(condition = dados_form['condition'],name = dados_form['name'],command = dados_form['command'])
            report.save()
            
            # Valores para tabela na pagina principal
            commands = Command.objects.all()
            computers = Computer.objects.all()

            return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands, "event": 1, "msg": "Report editado com sucesso."})


        return render(req, self.template_name, {'form' : form })