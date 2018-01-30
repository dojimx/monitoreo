from django.urls import path,include 
from apps.usuario.views import UsuarioList,UsuarioCreate, UsuarioUpdate, UsuarioDelete
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',   login_required(UsuarioList.as_view()), name='usuario_listar'),
   path('nuevo/', login_required(UsuarioCreate.as_view()), name='usuario_crear'),
   path('listar/', login_required(UsuarioList.as_view()), name='usuario_listar'),
   path('editar/<pk>/', login_required(UsuarioUpdate.as_view()), name='usuario_editar'),
   path('eliminar/<pk>/', login_required(UsuarioDelete.as_view()), name='usuario_eliminar')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
