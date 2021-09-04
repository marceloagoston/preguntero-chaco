from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages
from Apps.preguntas.models import Pregunta, OpcionPregunta

from Apps.usuarios.models import Usuario
import random

from .models import Juego

from .forms import JuegoForm, PartidaForm

class JuegosListView(LoginRequiredMixin, ListView):
    model = Juego
    template_name = 'juego/listapartidas.html'
    context_object_name = 'listaPartidas'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['listaPartidas'] = Juego.objects.filter(jugador=self.request.user)

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

        items = list(Pregunta.objects.filter(dificultad=f.dificultad))
        
        f.jugador = self.request.user

        f = form.save(commit=True)

        # change 3 to how many random items you want
        f.preguntas.set(random.sample(items, 5))
        

        
        return super(JuegoCreateView, self).form_valid(form)

class JuegoUpdateView(LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = 'juego/jugar.html'
    form_class = PartidaForm
    login_url = 'login'
    
    def get_success_url(self):
        return reverse_lazy('mis_partidas')
        
    def form_valid(self, form):
        
        f = form.save(commit=False)

        formValues = []

        for x in self.request.POST:
            formValues.append(self.request.POST.get(x, None))

        formValues.pop(0)

        correctas = 0
        for clave in formValues:
            if(OpcionPregunta.objects.get(pk=clave).correcta):
                correctas +=1

        if correctas < 4:
            f.puntos = 0
            messages.success(self.request, "Juego finalizado, Perdiste... Seguí participando 😥")
        elif correctas == 4:
            messages.success(self.request, "BUENAAA ¡¡Ganaste!! 😁")
            f.puntos = int(self.object.dificultad)
        else:
            messages.success(self.request, "IMPRESIONANTEEE!! 5/5 aciertooos! 🥳")
            f.puntos = int(self.object.dificultad) * 2

        f.finalizado = True
        
        return super(JuegoUpdateView, self).form_valid(form)
