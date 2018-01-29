from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.usuario.models import Usuario
from apps.usuario.forms import UsuarioForm


# Create your views here.

def index(request):
	return render(request, 'usuario/index.html')

def editar(request):
	return render(request, 'usuario/editar.html')	

def eliminar(request):
	return render(request, 'usuario/eliminar.html')
		
def listar(request):
	return render(request, 'usuario/listar.html')


class UsuarioList(ListView):
	model = Usuario
	template_name = 'usuario/listar.html'

class UsuarioCreate(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/nuevo.html'
	success_url = reverse_lazy ('usuario_listar')

class UsuarioUpdate(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/nuevo.html'
	success_url = reverse_lazy ('usuario_listar')

class UsuarioDelete(DeleteView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/eliminar.html'
	success_url = reverse_lazy ('usuario_listar')
