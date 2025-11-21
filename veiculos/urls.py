from django.urls import path
from . import views

app_name = 'veiculos' 

urlpatterns = [
    path('', views.VeiculoListView.as_view(), name='veiculo_list'),
    
    path('novo/', views.VeiculoCreateView.as_view(), name='veiculo_create'),
    
    path('editar/<int:pk>/', views.VeiculoUpdateView.as_view(), name='veiculo_update'),
    
    path('remover/<int:pk>/', views.VeiculoDeleteView.as_view(), name='veiculo_delete'),
]