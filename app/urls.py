from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as votar


app_name = 'kpop'

urlpatterns = [
    path('', votar.Home.as_view(), name='home'),
    path('sobre', votar.Sobre.as_view(), name='sobre'),
    path('foto', votar.Foto.as_view(), name='imagens'),
    path('contato', votar.Contato.as_view(), name='contato'),
    
]