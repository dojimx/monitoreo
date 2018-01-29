from django.db import models


class Usuario(models.Model):
	SEX = (
		('M', 'Masculino'),
		('F', 'Femenino'),)
	ROL = (
		('C', 'Capturista'),
		('A', 'Analista'),
		('ADM', 'Administrador'),)

	nombre = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	sexo = models.CharField(null= True, blank=True, max_length=1, choices=SEX)
	correo = models.EmailField()
	telefono = models.CharField(max_length=14)
	rol = models.CharField(null=True, blank=True, max_length=1, choices=ROL)


	def __str__(self):
		return self.nombre
	

