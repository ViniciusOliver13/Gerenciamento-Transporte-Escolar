from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    """
    Classe abstrata que contém os dados comuns a todas as pessoas do sistema.
    Não cria tabela no banco de dados (abstract = True).
    """
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True  # Isso define que é uma classe abstrata no Django

    def __str__(self):
        return self.nome

class Gestor(Usuario):
    # Herda de Usuario, então já tem nome, cpf, etc.
    
    # Vinculo com o login do sistema (Opcional, mas recomendado para quem loga)
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gestor_profile', null=True, blank=True)
    
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"Gestor: {self.nome}"

class Motorista(Usuario):
    # Herda de Usuario
    
    # Vinculo com o login do sistema
    user_auth = models.OneToOneField(User, on_delete=models.CASCADE, related_name='motorista_profile', null=True, blank=True)
    
    cnh = models.CharField(max_length=20, unique=True)
    data_validade_cnh = models.DateField()

    def __str__(self):
        return f"Mot. {self.nome} (CNH: {self.cnh})"

