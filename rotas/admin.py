from django.contrib import admin
from .models import Rota, Checklist, ConfirmacaoViagem, Ocorrencia

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'veiculo', 'motorista')
    list_filter = ('turno',)
    filter_horizontal = ('alunos',) # Facilita adicionar vários alunos

@admin.register(ConfirmacaoViagem)
class ConfirmacaoViagemAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'rota', 'data_viagem', 'data_confirmacao')
    list_filter = ('data_viagem', 'rota')
    search_fields = ('aluno__nome',) # Permite buscar pelo nome do aluno

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('rota', 'motorista', 'data', 'realizado')
    list_filter = ('data', 'realizado')
    filter_horizontal = ('alunos_presentes',) # Caixa dupla para marcar quem veio

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'veiculo', 'motorista', 'data_registro', 'resolvido')
    list_filter = ('tipo', 'resolvido')
    # Permite marcar como resolvido direto na lista
    list_editable = ('resolvido',)