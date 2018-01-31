from django.urls import path,include
from apps.medio.views import MedioList, MedioCreate, MedioUpdate, MedioDelete
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [
   path('',  login_required(MedioList.as_view()), name='medio_listar'),
   path('nuevo/', login_required(MedioCreate.as_view()), name='medio_crear'),
   path('listar/', login_required(MedioList.as_view()), name='medio_listar'),
   path('editar/<pk>/', login_required(MedioUpdate.as_view()), name='medio_editar'),
   path('eliminar/<pk>/', login_required(MedioDelete.as_view()), name='medio_eliminar')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
