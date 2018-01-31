from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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

# Create your views here.
