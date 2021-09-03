from django import forms

from .models import Juego

class JuegoForm(forms.ModelForm):

	class Meta:
		model = Juego
		fields = ['dificultad',]

	def __init__(self, *args, **kwargs):

		super(JuegoForm , self).__init__(*args, **kwargs)
		
		self.fields['dificultad'].widget.attrs['class'] = 'form-control'