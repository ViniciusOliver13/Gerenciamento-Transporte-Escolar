from django.urls import path
from . import views

# Define o namespace da app
app_name = 'usuarios'

urlpatterns = [
    # Página inicial do sistema
    path('', views.HomeView.as_view(), name='home'),
    path('redirect/', views.redirect_usuario, name='redirect_usuario'),
    path('painel-motorista/', views.painel_motorista, name='painel_motorista'),
]
