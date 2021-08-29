from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import models
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = ('username', 'email', 'nacimiento',)

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nacimiento',)