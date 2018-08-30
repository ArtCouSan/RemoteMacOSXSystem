from django.shortcuts import render, redirect
from perfis.models import *
from computer.models import *

def login(req):
    return render(req, 'login.html')

# Direciona para pagina principal

def home(req, user_id):

    user = User.objects.get(id=user_id)
    computers = Computer.objects.all()
    commands = Command.objects.all()

    return render(req, 'pagina_principal.html', { "user" : user , "computers": computers,"commands": commands})

