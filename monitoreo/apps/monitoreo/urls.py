from django.urls import path,include
from apps.monitoreo.views import MonitoreoList, MonitoreoCreate, MonitoreoUpdate, MonitoreoDelete
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [
   path('',  login_required(MonitoreoList.as_view()), name='monitoreo_listar'),
   path('nuevo/', login_required(MonitoreoCreate.as_view()), name='monitoreo_crear'),
   path('listar/', login_required(MonitoreoList.as_view()), name='monitoreo_listar'),
   path('editar/<pk>/', login_required(MonitoreoUpdate.as_view()), name='monitoreo_editar'),
   path('eliminar/<pk>/', login_required(MonitoreoDelete.as_view()), name='monitoreo_eliminar')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
