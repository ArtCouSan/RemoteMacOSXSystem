from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from command.models import Command
from computer.models import Computer
from django.contrib.auth.decorators import login_required
from pexpect import pxssh
import json
import sys, errno

def login(req):
    return render(req, 'login.html')


class HomeSSHView(TemplateView):

    template_name = 'pagina_principal.html'

    def get(self, req):

        commands = Command.objects.all()
    
        computers = Computer.objects.all()

        return render(req, self.template_name, { "computers": computers,"commands": commands})


    def post(self, req):

        commands = Command.objects.all()
    
        computers = Computer.objects.all()

        if req.method == 'POST':

            s = pxssh.pxssh()
            computersArrays = []
            commandsArrays = []
        
            computersIdArrays = req.POST.getlist('computers[]')
            commandsIdArrays = req.POST.getlist('commands[]')

            for cpId in computersIdArrays:
                i = Computer.objects.get(id = cpId)
                computersArrays.append(i)

            for cmId in commandsIdArrays:
                k = Command.objects.get(id = cmId)
                commandsArrays.append(k)

            for cp in computersArrays:
                #user = cp.user
                #hostname = cp.name
                #password = cp.password
                try:
                    if s.login("192.168.0.105", "arthur", "1998"):
                        s.sendline("say hello")
                        s.prompt
                except IOError as e:
                    if e.errno == errno.EPIPE:
                        print("Erro")
                

            return render(req, self.template_name, { "computers": computers,"commands": commands})
            
        else:
            
            return render(req, self.template_name, { "computers": computers,"commands": commands})

