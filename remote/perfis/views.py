from django.shortcuts import render
from perfis.models import User 

def login(req):
    return render(req, 'login.html')

def home(req, user_id):

    user = User.objects.get(id=user_id)

    return render(req, 'pagina_principal.html', { "user" : user })