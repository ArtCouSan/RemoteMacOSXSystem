from django.urls import path
from django.contrib import admin
from computer.views import ComputerViewAdd, ComputerViewEdit
from . import views

urlpatterns = [
    # Edit Computadores
    path('computerEdit/<int:computer_id>',  ComputerViewEdit.as_view(), name="computerEdit"),
    # Add Computadores
    path('computerAdd/', ComputerViewAdd.as_view(), name='computerAdd'),
    # Remove Computadores
    path('computerRemove/<int:computer_id>', views.computerRemove, name='computerRemove')
]