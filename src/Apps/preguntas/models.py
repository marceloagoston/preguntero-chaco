from django.db import models
from Apps.core.models import TimeStampedModel
from django.utils.text import slugify

# Categorias
# 1 Geografia
# 2 Naturaleza
# 3 Politica
# 4 Cultura

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	slug=models.SlugField(default='Nada')
	
	class Meta:
		db_table = 'Categorias'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs) 
		
	def __str__(self):
		return self.nombre[:50]

class Pregunta(TimeStampedModel):
	nombre = models.CharField(max_length=250)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	select_tipo = [
	    ('1', 'Fácil'),
	    ('2', 'Media'),
	    ('3','Difícil'),
    ]
	dificultad = models.CharField(max_length=1,choices=select_tipo,default='1')

	class Meta:
		db_table = 'Preguntas'

	def __str__(self):
		return self.nombre[:50]


class OpcionPregunta(models.Model):
	consigna = models.CharField(max_length=250)
	correcta = models.BooleanField(default=False)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'Opciones_Preguntas'

	def __str__(self):
		return self.consigna[:50]
