from django.shortcuts import render
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
<<<<<<< HEAD
=======

from apps.medio.models import Medio
>>>>>>> 445cf418a2fd278d1e9a4dffbb4bd9d411aa6b97
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




    

=======
<<<<<<< HEAD



	def Monitoreo(request): 
        form = TituloForm(request.GET or None), 
        if form.is_valid(): 
                fecha_desde = form.cleaned_data['fecha_desde'] 
                fecha_hasta = form.cleaned_data['fecha_hasta'] 

                monitoreo = monitoreo.objects.filter(fecha__range=(fecha_desde, 
fecha_hasta)) 

=======
	
>>>>>>> f7119f800b4f5615eff5c56e629a45a0e3593a2d
# Create your views here.
>>>>>>> 445cf418a2fd278d1e9a4dffbb4bd9d411aa6b97
