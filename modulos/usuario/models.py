from django.db import models

# Create your models here.

class Usuario(models.Model):
	SEX = (
		('M', 'MASCULINO'),
		('F', 'FEMENINO'),
		)

	nombre = models.CharField(max_length=50)
	apellido_parterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	sexo = models.CharField(max_length=1, choices=SEX)
	telefono = models.CharField(max_length=12)
	medio = models.ForeignKey(Medio, blank=True, null=True, on_delete=models.CASCADE)
	
	def __str__ (self):
		return self.nombre

class Medio(models.Model):
	TYPE = (
		('EST', 'ESTATAL'),
		('NAL', 'NACIONAL'),
		('INT', 'INTERNACIONAL'),
		)

	nombre = models.CharField(max_length=50)
	website = models.CharField(max_length=100)
	descript = models.CharField(max_length=500)
	tipo = models.CharField(max_length=3, choices=TYPE)
	usuario = models.OneToOneField(Usuario, blank=True, null=True, on_delete=models.CASCADE)
