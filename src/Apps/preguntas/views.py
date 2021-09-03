from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse

from .models import OpcionPregunta, Pregunta

from .forms import PreguntaForm, OpcionPreguntaForm

class PreguntasListView(LoginRequiredMixin, ListView):
	model = Pregunta
	template_name = 'preguntas/admin/listapreguntas.html'
	context_object_name = 'listaPreguntas'
	login_url = 'login'

class PreguntaCreateView(LoginRequiredMixin, CreateView):
	model = Pregunta
	template_name = 'preguntas/admin/altapregunta.html'
	form_class = PreguntaForm
	login_url = 'login'
	
	def form_valid(self, form):
		f = form.save(commit=True)

		messages.success(self.request, "Pregunta registrada exitosamente")
		self.success_url = reverse_lazy('editar_pregunta' , kwargs={'pk':f.id})
		
		return super(PreguntaCreateView, self).form_valid(form)

	# def get_success_url(self):
	# 	messages.success(self.request, "Pregunta registrada exitosamente")
	# 	return reverse_lazy('lista_preguntas')

class PreguntaUpdateView(LoginRequiredMixin, UpdateView):
	model = Pregunta
	template_name = 'preguntas/admin/editarpregunta.html'
	form_class = PreguntaForm
	login_url = 'login'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['opcionesPregunta'] = OpcionPregunta.objects.filter(pregunta=Pregunta.objects.get(pk=self.kwargs['pk']))

		print(context['opcionesPregunta'])

		context['formOpcionesPregunta'] = OpcionPreguntaForm()
		
		return context

	def get_success_url(self):
		messages.success(self.request, "Pregunta editada exitosamente")
		return reverse_lazy('lista_preguntas')

class PreguntaDeleteView(LoginRequiredMixin, DeleteView):
	model = Pregunta
	template_name = 'preguntas/admin/eliminarpregunta.html'
	login_url = 'login'

	def get_success_url(self):
		messages.success(self.request, "Pregunta eliminada exitosamente")
		return reverse_lazy('lista_preguntas')

def agregarOpcionPregunta(request, id_pregunta):
	print('consigna')
	print(request.POST.get('consigna'))
	print('correcta?')
	print(request.POST.get('correcta'))
	print('ID pregunta')
	print(id_pregunta)

	correcta = False
	consigna=request.POST.get('consigna')
	if(request.POST.get('correcta')):
		correcta=True
	pregunta=id_pregunta

	OpcionPregunta.objects.create(consigna=consigna, correcta=correcta, pregunta=Pregunta.objects.get(pk=pregunta))

	return JsonResponse({
		'content':{
			'message': ' Registrando opción de pregunta... ',
		}
	})