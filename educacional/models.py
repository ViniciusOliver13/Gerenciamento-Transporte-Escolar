from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Usuario

class Aluno(Usuario):
    # Herda nome, cpf, data_nascimento, endereco de 'Usuario'

    user_auth = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='aluno_profile',
        null=True, 
        blank=True
    )
    
    class StatusAluno(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo'
        INATIVO = 'INATIVO', 'Inativo'
        PENDENTE_RENOVACAO = 'PENDENTE_RENOVACAO', 'Pendente Renovação'

    matricula = models.CharField(max_length=20, unique=True)
    escola = models.CharField(max_length=200)

    declaracao_escolar = models.FileField(upload_to='declaracoes_escolares/', blank=True, null=True)
    
    data_validade_cadastro = models.DateField(null=True, blank=True, help_text="Data para renovação semestral")

    
    status_aluno = models.CharField(
        max_length=20, 
        choices=StatusAluno.choices,
        default=StatusAluno.ATIVO
    )

    def __str__(self):
        return f"{self.nome} (Mat: {self.matricula})"
