from django import forms
from apps.usuario.models import Usuario


class UsuarioForm(forms.ModelForm):

	class Meta: 
		model = Usuario 

		fields = [
			'nombre',
			'apellido_paterno',
			'apellido_materno',
			'sexo',
			'correo',
			'telefono',
			
		]
		labels = {
			'nombre' : 'Nombre',
			'apellido_paterno' : 'Apellido Paterno',
			'apellido_materno' : 'Apellido Materno',
			'sexo' : 'Sexo',
			'correo' : 'Correo',
			'telefono' : 'Telefono',
			
					}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'apellido_paterno' : forms.TextInput(attrs={'class' : 'form-control'}),
			'apellido_materno' : forms.TextInput(attrs={'class' : 'form-control'}),
			'sexo' : forms.Select(attrs={'class' : 'form-control'}),
			'correo' : forms.TextInput(attrs={'class' : 'form-control'}),
			'telefono' : forms.TextInput(attrs={'class' : 'form-control'}),
		}