from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.VeiculoListView.as_view(), name='veiculo_list'),
    
    path('novo/', views.VeiculoCreateView.as_view(), name='veiculo_create'),
    
    path('<int:pk>/editar/', views.VeiculoUpdateView.as_view(), name='veiculo_update'),
    
    path('<int:pk>/deletar/', views.VeiculoDeleteView.as_view(), name='veiculo_delete'),
]