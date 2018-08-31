from django.shortcuts import render, redirect
from perfis.models import *
from command.models import Command
from computer.models import Computer
from django.contrib.auth.decorators import login_required


def login(req):
    return render(req, 'login.html')

# Direciona para pagina principal
@login_required
def home(req):

    commands = Command.objects.all()
    
    computers = Computer.objects.all()

    return render(req, 'pagina_principal.html', { "computers": computers,"commands": commands})

