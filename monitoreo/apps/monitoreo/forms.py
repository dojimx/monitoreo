from django import forms
from apps.monitoreo.models import Monitoreo 




class MonitoreoForm(forms.ModelForm):

	class Meta: 
		model = Monitoreo

		fields = [
			'titulo',
			'url',
			'publicacion',
			'descripcion',
			'fecha_publicacion',
			'medio',
			
		]
		labels = {
			'titulo': 'Titulo',
			'url' : 'URL',
			'publicacion': 'Publicacion',
			'descripcion' : 'Descripcion',
			'fecha_publicacion' : 'Fecha de publicacion',
			'medio' : 'Medio',
			
		}
		widgets = {
			'titulo' : forms.TextInput(attrs={'class' : 'form-control'}),
			'url' : forms.URLInput(attrs={'class' : 'form-control'}),
			'publicacion' : forms.Select(attrs={'class' : 'form-control'}),
			'descripcion' : forms.Textarea(attrs={'class' : 'form-control'}),
			'fecha_publicacion' : forms.SelectDateWidget(attrs={'class' : 'datepicker'}),
			'medio' : forms.Select(attrs={'class' : 'form-control'}),
			
		}
		
		