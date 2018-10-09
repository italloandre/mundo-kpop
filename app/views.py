from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

class Home(TemplateView):
	template_name = 'home.html'

class Contato(CreateView):
	model = models.Contato
	template_name='contato.html'
	success_url = reverse_lazy('core:Home')
	fields = ['email', 'texto', 'assunto']

class Sobre(TemplateView):
	template_name = 'home.html'

class Foto(TemplateView):
	template_name = 'foto.html'
# Create your views here.
