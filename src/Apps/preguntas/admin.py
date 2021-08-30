from django.contrib import admin

from .models import Pregunta, OpcionPregunta, Categoria

admin.site.register(Pregunta)
admin.site.register(OpcionPregunta)
admin.site.register(Categoria)