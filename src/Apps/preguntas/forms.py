from django import forms

from .models import Pregunta, OpcionPregunta

class PreguntaForm(forms.ModelForm):

	class Meta:
		model = Pregunta
		fields = ['nombre', 'categoria', 'dificultad']

	def __init__(self, *args, **kwargs):

		super(PreguntaForm , self).__init__(*args, **kwargs)
		
		self.fields['nombre'].widget.attrs['class'] = 'form-control'
		self.fields['categoria'].widget.attrs['class'] = 'form-control'
		self.fields['dificultad'].widget.attrs['class'] = 'form-control'

class OpcionPreguntaForm(forms.ModelForm):

	class Meta:
		model = OpcionPregunta
		fields = ['consigna', 'correcta']

	def __init__(self, *args, **kwargs):

		super(OpcionPreguntaForm , self).__init__(*args, **kwargs)
		
		self.fields['consigna'].widget.attrs['class'] = 'form-control'
		self.fields['correcta'].widget.attrs['class'] = 'form-control'