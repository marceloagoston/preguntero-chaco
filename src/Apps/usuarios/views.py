from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Usuario
from .forms import UsuarioCreationForm


class RegistroView(CreateView):
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'admin/usuarios/listausuarios.html'
    context_object_name = 'listaUsuarios'
    login_url = 'login'