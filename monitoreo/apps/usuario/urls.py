from django.urls import path,include
from apps.usuario.views import index,editar,eliminar,UsuarioList,UsuarioCreate, UsuarioUpdate, UsuarioDelete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('', index),
   path('nuevo/', UsuarioCreate.as_view(), name='usuario_crear'),
   path('listar/', UsuarioList.as_view(), name='usuario_listar'),
   path('editar/<pk>/', UsuarioUpdate.as_view(), name='usuario_editar'),
   path('eliminar/<pk>/', UsuarioDelete.as_view(), name='usuario_eliminar')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
