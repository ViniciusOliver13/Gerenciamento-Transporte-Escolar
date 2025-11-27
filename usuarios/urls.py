from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('redirect/', views.redirect_usuario, name='redirect_usuario'),
    path('painel-motorista/', views.painel_motorista, name='painel_motorista'),

    path('motoristas/', views.MotoristaListView.as_view(), name='motorista_list'),
    
    path('motoristas/novo/', views.MotoristaCreateView.as_view(), name='motorista_create'),
    
    path('motoristas/<int:pk>/editar/', views.MotoristaUpdateView.as_view(), name='motorista_update'),

    path('motoristas/<int:pk>/deletar/', views.MotoristaDeleteView.as_view(), name='motorista_delete'),
]
