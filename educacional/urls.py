# educacional/urls.py
from django.urls import path
from .views import AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView

urlpatterns = [
    path('', AlunoListView.as_view(), name='aluno_list'),
    path('novo/', AlunoCreateView.as_view(), name='aluno_create'),
    path('editar/<int:pk>/', AlunoUpdateView.as_view(), name='aluno_update'),
    path('deletar/<int:pk>/', AlunoDeleteView.as_view(), name='aluno_delete'),
]