from django.urls import path,include
from apps.medio.views import index,editar,eliminar,MedioList,MedioCreate, MedioUpdate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', index),
   path('nuevo/', MedioCreate.as_view(), name='medio_crear'),
   path('listar/', MedioList.as_view(), name='medio_listar'),
   path('editar/<pk>/', MedioUpdate.as_view(), name='medio_editar'),
   path('eliminar/', eliminar)
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
