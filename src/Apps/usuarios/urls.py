from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('lista-usuarios/', views.UsuarioListView.as_view(), name='lista_usuarios'),

]