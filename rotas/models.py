from django.db import models

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

    horario_inicio = models.TimeField(
        help_text="Horário de saída do ponto inicial",)
    
    prazo_limite_confirmacao = models.TimeField(
        help_text="Horário limite para o aluno confirmar",)

    # 3. Associações (Relacionamentos)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True, blank=True)
    alunos = models.ManyToManyField(Aluno, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.get_turno_display()}"


class ConfirmacaoViagem(models.Model):
    """
    O Aluno cria esse registro para dizer: "Vou amanhã de manhã".
    O Gestor usa isso para ver a demanda (RF-11).
    """
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    data_viagem = models.DateField()
    data_confirmacao = models.DateTimeField(auto_now_add=True) # Quando ele clicou
    
    class Meta:
        unique_together = ('aluno', 'rota', 'data_viagem') # Evita duplicar confirmação pro mesmo dia
        verbose_name = "Confirmação de Viagem"
        verbose_name_plural = "Confirmações de Viagem"

    def __str__(self):
        return f"{self.aluno.nome} - {self.rota.nome} ({self.data_viagem})"


class Checklist(models.Model):
    """
    O Motorista abre isso na hora do embarque.
    """
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True) # Quem fez a chamada
    data = models.DateField(auto_now_add=True)
    
    # Aqui salvamos QUEM estava presente de fato.
    # A lógica no Frontend será: Mostrar quem fez 'ConfirmacaoViagem' e o motorista marca quem entrou.
    alunos_presentes = models.ManyToManyField(Aluno, blank=True, related_name='presencas')
    
    realizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Checklist {self.rota.nome} - {self.data}"
    

class Ocorrencia(models.Model):
    """
    Registra problemas no veículo ou aluno que não embarcou (mas tinha confirmado).
    """
    TIPO_OCORRENCIA = [
        ('ALUNO_AUSENTE', 'Aluno Confirmou mas não Embarcou'),
        ('PROBLEMA_MECANICO', 'Problema Mecânico no Veículo'),
        ('ATRASO', 'Atraso na Rota'),
        ('OUTRO', 'Outro'),
    ]

    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, null=True, blank=True) # Vincula ao dia
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True)
    
    tipo = models.CharField(max_length=30, choices=TIPO_OCORRENCIA)
    descricao = models.TextField(help_text="Descreva o problema ou liste os alunos faltantes")
    data_registro = models.DateTimeField(auto_now_add=True)
    
    # Campo para o Gestor marcar que viu o alerta
    resolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"Alerta: {self.get_tipo_display()} - {self.data_registro}"