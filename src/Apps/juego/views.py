from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages
from Apps.preguntas.models import Pregunta

from Apps.usuarios.models import Usuario
import random

from .models import Juego

from .forms import JuegoForm

class JuegosListView(LoginRequiredMixin, ListView):
    model = Juego
    template_name = 'juego/listapartidas.html'
    context_object_name = 'listaPartidas'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['listaPartidas'] = Juego.objects.filter(jugador=self.request.user)
        print(context['listaPartidas'])

        return context

class JuegoCreateView(LoginRequiredMixin, CreateView):
    model = Juego
    template_name = 'juego/nuevojuego.html'
    form_class = JuegoForm
    login_url = 'login'
    
    def get_success_url(self):
        messages.success(self.request, "Partida registrada exitosamente")
        return reverse_lazy('mis_partidas')
        
    def form_valid(self, form):
        
        f = form.save(commit=False)

        print(f.dificultad)

        items = list(Pregunta.objects.filter(dificultad=f.dificultad))
        
        f.jugador = self.request.user

        f = form.save(commit=True)

        # change 3 to how many random items you want
        f.preguntas.set(random.sample(items, 1))
        

        
        return super(JuegoCreateView, self).form_valid(form)
