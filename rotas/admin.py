from django.contrib import admin
from .models import Rota, Checklist

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'veiculo', 'motorista')
    list_filter = ('turno',)
    # Facilita adicionar muitos alunos (caixa de seleção dupla)
    filter_horizontal = ('alunos',) 

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('rota', 'data', 'realizado')
    list_filter = ('realizado', 'data')