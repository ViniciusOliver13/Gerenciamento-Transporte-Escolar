from django.contrib import admin
from .models import Motorista, Gestor

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    # Se o nome do seu campo no model for 'user_auth', use ele aqui
    list_display = ('get_nome', 'cnh', 'data_validade_cnh')
    
    def get_nome(self, obj):
        # Verifica se existe um usuário vinculado antes de tentar acessar
        if obj.user_auth:
            return obj.user_auth.first_name
        return "--- Sem Usuário ---"
    
    get_nome.short_description = 'Nome'

@admin.register(Gestor)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('get_nome', 'cargo')
    
    def get_nome(self, obj):
        if obj.user_auth:
            return obj.user_auth.first_name
        return "--- Sem Usuário ---"
        
    get_nome.short_description = 'Nome'