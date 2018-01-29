from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.usuario.models import Usuario
from apps.usuario.forms import UsuarioForm


# Create your views here.



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
