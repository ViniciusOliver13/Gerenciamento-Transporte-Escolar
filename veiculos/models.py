from django.db import models
from usuarios.models import Motorista

class Veiculo(models.Model):
    
    placa = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="placa do veiculo"
    )
    
    modelo = models.CharField(
        max_length=50,
        verbose_name="modelo do veiculo (exemplo: onibus, van, carro)"
    )

    capacidade = models.PositiveIntegerField(
        verbose_name="capacidade de passageiros"
    )
    
    motorista = models.ForeignKey(
        Motorista,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="motorista responsavel pelo veiculo"
    )
    
    class Meta:
        verbose_name = "veiculo"
        verbose_name_plural = "veiculos"
        
    def __str__(self):
        return f"{self.modelo} - {self.placa} ({self.capacidade} passageiros)"