from django.db import models
from Apps.core.models import TimeStampedModel
from Apps.preguntas.models import Pregunta
from Apps.usuarios.models import Usuario

class Juego(TimeStampedModel):
    finalizado = models.BooleanField(default=False)
    jugador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    preguntas = models.ManyToManyField(Pregunta, related_name="Preguntas_del_Juego")
    
    select_tipo = [
	    ('1', 'Fácil'),
	    ('2', 'Media'),
	    ('3','Difícil'),
    ]
    dificultad = models.CharField(max_length=1,choices=select_tipo,default='1')
    puntos = models.PositiveBigIntegerField(default=0)
    
    class Meta:
        db_table = 'Juegos'
        
    def __str__(self):
        return str(self.id)