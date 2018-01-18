from medio.models import Medio 



class MedioForm(forms.ModelForm):

	class Meta: 
		model = Medio 

		fields = [
			'nombre',
			'url',
			'tipo',
			'usuario',
			
		]
		labels = {
			'nombre' : 'Nombre',
			'url' : 'URL',
			'tipo' : 'Tipo',
			'usuario' : 'Usuario',
			
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'url' : forms.TextInput(attrs={'class' : 'form-control'}),
			'tipo' : forms.TextInput(attrs={'class' : 'form-control'}),
			'usuario' : forms.Select(attrs={'class' : 'form-control'}),
			
		}