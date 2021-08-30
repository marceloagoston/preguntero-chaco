from django import forms

from .models import Pregunta

class PreguntaForm(forms.ModelForm):

	class Meta:
		model = Pregunta
		fields = ['nombre', 'categoria', 'dificultad']

	def __init__(self, *args, **kwargs):

		super(PreguntaForm , self).__init__(*args, **kwargs)
		
		self.fields['nombre'].widget.attrs['class'] = 'form-control'
		self.fields['categoria'].widget.attrs['class'] = 'form-control'
		self.fields['dificultad'].widget.attrs['class'] = 'form-control'