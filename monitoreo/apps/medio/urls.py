from django.urls import path,include
from apps.medio.views import index,listar,editar,eliminar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', index),
   path('listar/', listar),
   path('editar/', editar),
   path('eliminar/', eliminar)
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
