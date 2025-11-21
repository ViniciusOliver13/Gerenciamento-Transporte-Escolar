from django.db import models

class Veiculo(models.Model):
    # Campos definidos no diagrama
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    capacidade = models.IntegerField()
    

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
