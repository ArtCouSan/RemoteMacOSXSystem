from django.shortcuts import render, redirect
from perfis.models import *

def login(req):
    return render(req, 'login.html')

def home(req, user_id):

    user = User.objects.get(id=user_id)
    computers = Computer.objects.all()
    commands = Command.objects.all()

    return render(req, 'pagina_principal.html', { "user" : user , "computers": computers,"commands": commands})

def computerEdit(req, computer):

    return render(req, 'pagina_computer.html', {"computer": computer })