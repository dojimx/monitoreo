from django.db import models
from django.db.models.signals import pre_save, post_save
from apps.usuario.models import Usuario
from django.conf import settings


class Medio(models.Model):
	NOTICE = (
		('EST', 'ESTATAL'),
		('NAC', 'NACIONAL'),
		('INT', 'INTERNACIONAL'),
		)
	nombre = models.CharField(max_length=50)
	url = models.URLField(max_length=50)
	tipo = models.CharField(max_length=3, choices=NOTICE)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

	

	def __str__(self):
		return self.nombre


