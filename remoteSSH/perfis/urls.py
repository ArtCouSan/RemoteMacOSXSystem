from django.urls import include,  path
from django.contrib import admin
from perfis.views import HomeSSHView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login
    path('', auth_views.LoginView.as_view(template_name='login.html'),  name='login'),
    # Logout
    path('logout/', auth_views.LogoutView.as_view(),  name='logout'),
    # Home
    path('home/',HomeSSHView.as_view(template_name="pagina_principal.html"), name='home')
]