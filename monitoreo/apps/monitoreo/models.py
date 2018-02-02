from django.db import models
from apps.medio.models import Medio
from django.conf import settings

# Create your models here.
class Monitoreo(models.Model):
	PUBL = (
		('POSITIVO', 'POSITIVO'),
		('NEUTRAL', 'NEUTRAL'),
		('NEGATIVO', 'NEGATIVO'),
		)
	titulo = models.CharField(null=True, blank=True, max_length=100)
	url = models.URLField(max_length=50)
	publicacion = models.CharField(max_length=8, choices=PUBL)
	descripcion = models.TextField()
	fecha_publicacion = models.DateField()
	medio = models.ForeignKey(Medio, null=True, blank=True, on_delete=models.CASCADE)


	


	def __str__(self):
		return self.titulo

		
