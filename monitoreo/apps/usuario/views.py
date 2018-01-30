from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.usuario.models import Usuario
from apps.usuario.forms import UsuarioForm


# Create your views here.



class UsuarioList(ListView):
	model = User
	form_class = UsuarioForm
	template_name = 'usuario/listar.html'


class UsuarioCreate(CreateView):
	model = User
	form_class = UsuarioForm
	template_name = 'usuario/nuevo.html'
	success_url = reverse_lazy ('usuario_listar')


class UsuarioUpdate(UpdateView):
	model = User
	form_class = UsuarioForm
	template_name = 'usuario/editar.html'
	success_url = reverse_lazy ('usuario_listar')

class UsuarioDelete(DeleteView):
	model = User
	form_class = UsuarioForm
	template_name = 'usuario/eliminar.html'
	success_url = reverse_lazy ('usuario_listar')
