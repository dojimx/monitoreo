from django.shortcuts import render


# Create your views here.

def index(request):
	return render(request, 'medio/index.html')

def editar(request):
	return render(request, 'medio/editar.html')	

def eliminar(request):
	return render(request, 'medio/eliminar.html')
		
def listar(request):
	return render(request, 'medio/listar.html')