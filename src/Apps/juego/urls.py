from django.urls import path
from . import views

urlpatterns = [
	path('Mis-partidas/', views.JuegosListView.as_view(), name='mis_partidas'),
	path('nuevo/', views.JuegoCreateView.as_view(), name='nuevo_juego'),
	# path('Admin/editar/<int:pk>/', views.PreguntaUpdateView.as_view(), name='editar_pregunta'),
	# # path('<int:pk>/', CaracteristicasDetailView.as_view(), name='detalle_caracteristica'),
	# path('Admin/eliminar/<int:pk>/', views.PreguntaDeleteView.as_view(), name='eliminar_pregunta'),

	# path('<int:id_pregunta>/agregar-opcion-pregunta/', views.agregarOpcionPregunta, name='agregar_opcion'),
]