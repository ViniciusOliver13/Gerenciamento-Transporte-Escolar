from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Painel administrativo do Django
    path('admin/', admin.site.urls),
    
    # Autenticação (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Apps do sistema
    path('', include('usuarios.urls')),              # Home e gestão de usuários
    path('alunos/', include('educacional.urls')),    # Gestão educacional (alunos)
    path('rotas/', include('rotas.urls')),           # Gestão de rotas de transporte
]

# Servir arquivos estáticos e de mídia apenas em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
