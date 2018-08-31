from django.shortcuts import render, redirect
from perfis.models import *
from command.models import Command
from computer.models import Computer

def login(req):
    return render(req, 'login.html')

# Direciona para pagina principal

def home(req, user_id):

    user = User.objects.get(id=user_id)

    commands = Command.objects.all()
    
    computers = Computer.objects.all()

    return render(req, 'pagina_principal.html', { "user" : user , "computers": computers,"commands": commands})

