from django.urls import path
from django.contrib import admin
from computer.views import ComputerViewAdd, ComputerViewEdit
from . import views

urlpatterns = [
    path('computerEdit/<int:computer_id>',  ComputerViewEdit.as_view(), name="computerEdit"),
    path('computerAdd/', ComputerViewAdd.as_view(), name='computerAdd'),
    path('computerRemove/', views.computerRemove, name='computerRemove')
]