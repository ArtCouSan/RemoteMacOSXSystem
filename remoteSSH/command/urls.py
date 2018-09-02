from django.urls import path
from django.contrib import admin
from . import views
from command.views import CommandViewEdit, CommandViewAdd

urlpatterns = [
    # Edit Comandos
    path('commandEdit/<int:command_id>', CommandViewEdit.as_view(), name="commandEdit"),
    # Add Comandos
    path('commandAdd/', CommandViewAdd.as_view(), name='commandAdd'),
    # Remove Computadores
    path('commandRemove/<int:command_id>', views.commandRemove, name='commandRemove')
]