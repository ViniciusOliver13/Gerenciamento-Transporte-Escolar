from django.urls import path
from . import views

# Define o namespace da app
app_name = 'usuarios'

urlpatterns = [
    # Página inicial do sistema
    path('', views.HomeView.as_view(), name='home'),
]
