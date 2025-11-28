from django.urls import path
from . import views

app_name = 'rotas'

urlpatterns = [
    # Listagem de rotas
    path('', views.RotaListView.as_view(), name='rota_list'),
    
    # Criar nova rota
    path('criar/', views.RotaCreateView.as_view(), name='rota_create'),
    
    # Editar rota
    path('<int:pk>/editar/', views.RotaUpdateView.as_view(), name='rota_update'),
    
    # Detalhes da rota (onde adiciona alunos)
    path('<int:pk>/', views.RotaDetailView.as_view(), name='rota_detail'),
    
    # Adicionar alunos em lote
    path('<int:pk>/adicionar-alunos/', views.AdicionarAlunosView.as_view(), name='adicionar_alunos'),
    
    # Remover aluno da rota
    path('<int:pk>/remover-aluno/<int:aluno_id>/', views.remover_aluno_rota, name='remover_aluno'),
    
    # Deletar rota
    path('<int:pk>/deletar/', views.RotaDeleteView.as_view(), name='rota_delete'),

    # Confirmar viagem
    path('<int:rota_id>/confirmar-viagem/', views.confirmar_viagem, name='confirmar_viagem'),

    path('<int:rota_id>/confirmar-viagem/<str:tipo>/', views.confirmar_viagem, name='confirmar_viagem'),
]
