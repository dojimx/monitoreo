from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.medio.models import Medio
from apps.medio.forms import MedioForm


# Create your views here.

def index(request):
	return render(request, 'medio/index.html')

def editar(request):
	return render(request, 'medio/editar.html')	

def eliminar(request):
	return render(request, 'medio/eliminar.html')
		
def listar(request):
	return render(request, 'medio/listar.html')


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
	template_name = 'medio/nuevo.html'
	success_url = reverse_lazy ('medio_listar')

