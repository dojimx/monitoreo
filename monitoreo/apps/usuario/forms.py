from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuario.models import Usuario


class UsuarioForm(UserCreationForm):

	class Meta: 
		model = User

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			
			
			
		]
		labels = {
			'username' : 'Usuario',
			'first_name' : 'Nombre',
			'last_name' : 'Apellido',
			'email' : 'Correo',

					}
		
		