from django.db import models

# Importando as classes dos outros apps (as "linhas" do diagrama)
from veiculos.models import Veiculo
from usuarios.models import Motorista
from educacional.models import Aluno

class Rota(models.Model):
    # 1. Enum Turno (Matutino, Vespertino, Noturno)
    class Turno(models.TextChoices):
        MATUTINO = 'MATUTINO', 'Matutino'
        VESPERTINO = 'VESPERTINO', 'Vespertino'
        NOTURNO = 'NOTURNO', 'Noturno'

    # 2. Atributos (Conforme sua definição)
    nome = models.CharField(max_length=100)
    
    turno = models.CharField(
        max_length=20, 
        choices=Turno.choices,
        default=Turno.MATUTINO
    )
    
    # Convertido de 'prazoLimiteConfirmacao' para o padrão Python (snake_case)
    prazo_limite_confirmacao = models.TimeField()

    # 3. Associações (Relacionamentos)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True, blank=True)
    alunos = models.ManyToManyField(Aluno, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.get_turno_display()}"

class Checklist(models.Model):
    # Mantive o Checklist pois ele depende da Rota
    data = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    realizado = models.BooleanField(default=False)
    
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)

    def __str__(self):
        return f"Checklist {self.rota.nome} - {self.data}"