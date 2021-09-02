from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages

from Apps.usuarios.models import Usuario

from .models import Juego

class PreguntasListView(LoginRequiredMixin, ListView):
    model = Juego
    template_name = 'juego/listapartidas.html'
    context_object_name = 'listaPartidas'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['listaPartidas'] = Juego.objects.filter(jugador=self.request.user)

        return context
