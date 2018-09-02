from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfis.urls')),
    path('', include('computer.urls')),
    path('', include('command.urls')),
]
