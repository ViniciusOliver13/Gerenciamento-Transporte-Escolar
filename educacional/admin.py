from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'escola', 'status_aluno')
    list_filter = ('status_aluno', 'escola') # Cria filtro lateral
    search_fields = ('nome', 'matricula', 'cpf')