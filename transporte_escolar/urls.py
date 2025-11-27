from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', include('usuarios.urls')),              # Home e gestão de usuários
    path('alunos/', include('educacional.urls')),    # Gestão educacional (alunos)
    path('rotas/', include('rotas.urls')),           # Gestão de rotas de transporte
    path('veiculos/', include('veiculos.urls')),     # Gestão de veículos
    path('motoristas/', include('usuarios.urls')),   # Gestão de motoristas
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
