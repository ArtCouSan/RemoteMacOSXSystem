from django.urls import path
from django.contrib import admin
from . import views
from command.views import CommandViewEdit, CommandViewAdd

urlpatterns = [
    path('commandEdit/<int:command_id>', CommandViewEdit.as_view(), name="commandEdit"),
    path('commandAdd/', CommandViewAdd.as_view(), name='commandAdd'),
    path('commandRemove/<int:command_id>', views.commandRemove, name='commandRemove')
]