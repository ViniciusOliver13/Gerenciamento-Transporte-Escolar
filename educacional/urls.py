from django.urls import path
from . import views

# Define o namespace da app
app_name = 'educacional'

urlpatterns = [
    # Listagem de alunos
    path('', views.AlunoListView.as_view(), name='aluno_list'),
    
    # Criar novo aluno
    path('novo/', views.AlunoCreateView.as_view(), name='aluno_create'),
    
    # Editar aluno existente
    path('<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    
    # Deletar aluno
    path('<int:pk>/deletar/', views.AlunoDeleteView.as_view(), name='aluno_delete'),
]
