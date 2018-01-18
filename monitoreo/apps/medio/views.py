from django.shortcuts import render
from django.views.generic import ListView
from medio.forms import MedioForm
from medio.models import Medio 
# Create your views here.

class MedioList(ListView):
	model = Medio
	template_name = 'medio/medio_list.html'
# Create your views here.
