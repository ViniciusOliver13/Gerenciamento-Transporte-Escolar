from django.db import models
# Importando a classe abstrata do app vizinho
from usuarios.models import Usuario

class Aluno(Usuario):
    # Herda nome, cpf, data_nascimento, endereco de 'Usuario'
    
    class StatusAluno(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo'
        INATIVO = 'INATIVO', 'Inativo'
        PENDENTE_RENOVACAO = 'PENDENTE_RENOVACAO', 'Pendente Renovação'

    matricula = models.CharField(max_length=20, unique=True)
    escola = models.CharField(max_length=200)
    
    status_aluno = models.CharField(
        max_length=20, 
        choices=StatusAluno.choices,
        default=StatusAluno.ATIVO
    )

    def __str__(self):
        return f"{self.nome} (Mat: {self.matricula})"
