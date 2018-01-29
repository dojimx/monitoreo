from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.medio.models import Medio
from apps.medio.forms import MedioForm


# Create your views here.

class MedioList(ListView):
	model = Medio
	template_name = 'medio/listar.html'

class MedioCreate(CreateView):
	model = Medio
	form_class = MedioForm
	template_name = 'medio/nuevo.html'
	success_url = reverse_lazy ('medio_listar')

class MedioUpdate(UpdateView):
	model = Medio
	form_class = MedioForm
	template_name = 'medio/editar.html'
	success_url = reverse_lazy ('medio_listar')

class MedioDelete(DeleteView):
	model = Medio
	form_class = MedioForm
	template_name = 'medio/eliminar.html'
	success_url = reverse_lazy ('medio_listar')
