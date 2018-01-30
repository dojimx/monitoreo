from django.urls import path,include
from apps.principal.views import Inicio
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings


urlpatterns = [
   path('',  Inicio, name='index_principal'),
   ]