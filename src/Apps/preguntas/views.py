from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Pregunta

from .forms import PreguntaForm

class PreguntasListView(LoginRequiredMixin, ListView):
	model = Pregunta
	template_name = 'preguntas/admin/listapreguntas.html'
	context_object_name = 'listaPreguntas'
	login_url = 'login'

class PreguntaCreateView(LoginRequiredMixin, CreateView):
	model = Pregunta
	template_name = 'preguntas/admin/altapregunta.html'
	form_class = PreguntaForm
	# fields = ['nombre', 'categoria', 'dificultad']
	success_url = reverse_lazy('lista_preguntas')
	login_url = 'login'

class PreguntaUpdateView(LoginRequiredMixin, UpdateView):
	model = Pregunta
	template_name = 'preguntas/admin/editarpregunta.html'
	form_class = PreguntaForm
	# fields = ['nombre', 'categoria', 'dificultad']
	success_url = reverse_lazy('lista_preguntas')
	login_url = 'login'

class PreguntaDeleteView(LoginRequiredMixin, DeleteView):
	model = Pregunta
	template_name = 'preguntas/admin/eliminarpregunta.html'
	success_url = reverse_lazy('lista_preguntas')
	login_url = 'login'