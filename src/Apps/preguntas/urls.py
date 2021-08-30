from django.urls import path
from . import views

urlpatterns = [
	path('Admin/Lista-preguntas/', views.PreguntasListView.as_view(), name='lista_preguntas'),
	path('Admin/nueva/', views.PreguntaCreateView.as_view(), name='nueva_pregunta'),
	path('Admin/editar/<int:pk>/', views.PreguntaUpdateView.as_view(), name='editar_pregunta'),
	# path('<int:pk>/', CaracteristicasDetailView.as_view(), name='detalle_caracteristica'),
	path('Admin/eliminar/<int:pk>/', views.PreguntaDeleteView.as_view(), name='eliminar_pregunta'),
]