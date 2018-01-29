from django.urls import path,include
from apps.medio.views import MedioList, MedioCreate, MedioUpdate, MedioDelete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',  MedioList.as_view(), name='medio_listar'),
   path('nuevo/', MedioCreate.as_view(), name='medio_crear'),
   path('listar/', MedioList.as_view(), name='medio_listar'),
   path('editar/<pk>/', MedioUpdate.as_view(), name='medio_editar'),
   path('eliminar/<pk>/', MedioDelete.as_view(), name='medio_eliminar')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
