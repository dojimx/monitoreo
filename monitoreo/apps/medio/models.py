from django.db import models

from apps.usuario.models import Usuario


class Medio(models.Model):
	NOTICE = (
		('EST', 'ESTATAL'),
		('NAC', 'NACIONAL'),
		('INT', 'INTERNACIONAL'),
		)
	nombre = models.CharField(max_length=50)
	url = models.URLField(max_length=50)
	tipo = models.CharField(max_length=3, choices=NOTICE)
	usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


