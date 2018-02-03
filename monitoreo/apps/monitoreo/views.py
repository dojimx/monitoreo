from django.shortcuts import render
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.medio.models import Medio
from apps.monitoreo.models import Monitoreo
from apps.monitoreo.forms import MonitoreoForm


# Create your views here.

class MonitoreoList(ListView):
	model = Monitoreo
	template_name = 'monitoreo/listar.html'

class MonitoreoCreate(CreateView):
	model = Monitoreo
	form_class = MonitoreoForm
	template_name = 'monitoreo/nuevo.html'
	success_url = reverse_lazy ('monitoreo_listar')

class MonitoreoUpdate(UpdateView):
	model = Monitoreo
	form_class = MonitoreoForm
	template_name = 'monitoreo/editar.html'
	success_url = reverse_lazy ('monitoreo_listar')

class MonitoreoDelete(DeleteView):
	model = Monitoreo
	form_class = MonitoreoForm
	template_name = 'monitoreo/eliminar.html'
	success_url = reverse_lazy ('monitoreo_listar')



<<<<<<< HEAD
=======
#def busqueda(request):
#    error = False
#    if 'date_from' and 'date_to'in request.GET:
#    	date_from = datetime.datetime.strptime(request.GET['q1'], '%d-%m-%Y')
#    	date_to = datetime.datetime.strptime(request.GET['q2'], '%d-%m-%Y')
#    	if not date_from:
#    		error = True
#    	elif not date_to:
#    		error = True
#    	else:
#    		m1 = Monitoreo.objects.filter(created__range=(date_from, date_to))
#    		return render(request, 'monitoreo/busquedaR.html', {'m1': m1 })
#    return render(request, 'monitoreo/busqueda.html')

=======
>>>>>>> e8ea0302ce338526f5d3a9b14ef6c09bad030d08

def b1(request):
    error = False
    if 'q1' and 'q2'in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']
        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            m1 = Monitoreo.objects.filter(fecha_publicacion__range=(q1,q2))
            return render(request, 'monitoreo/busquedaR.html',{'m1': m1 })
    return render(request, 'monitoreo/busqueda.html', {'error': error})

<<<<<<< HEAD
	def Monitoreo(request): 
        form = TituloForm(request.GET or None), 
        if form.is_valid(): 
                fecha_desde = form.cleaned_data['fecha_desde'] 
                fecha_hasta = form.cleaned_data['fecha_hasta'] 

                monitoreo = monitoreo.objects.filter(fecha__range=(fecha_desde, 
fecha_hasta)) 


>>>>>>> 93ac8ce77bf1f434268fb31051957bc01bfedffb
# Create your views here.
=======
>>>>>>> e8ea0302ce338526f5d3a9b14ef6c09bad030d08
