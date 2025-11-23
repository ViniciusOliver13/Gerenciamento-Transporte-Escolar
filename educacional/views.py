from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin # Importante para mensagens
from django.contrib import messages # Importante para o delete
from django.db.models import Q
from datetime import date
from .models import Aluno

class AlunoListView(ListView):
    model = Aluno
    template_name = 'educacional/aluno_list.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca')
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) | 
                Q(matricula__icontains=busca) | 
                Q(cpf__icontains=busca)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hoje'] = date.today()
        return context

# Adicionamos SuccessMessageMixin para enviar a mensagem no cadastro
class AlunoCreateView(SuccessMessageMixin, CreateView):
    model = Aluno
    template_name = 'educacional/aluno_form.html'
    fields = ['nome', 'cpf', 'data_nascimento', 'matricula', 'escola', 'data_validade_cadastro', 'declaracao_escolar', 'status_aluno']
    success_url = reverse_lazy('aluno_list')
    success_message = "Aluno %(nome)s cadastrado com sucesso! 🎉"

class AlunoUpdateView(SuccessMessageMixin, UpdateView):
    model = Aluno
    template_name = 'educacional/aluno_form.html'
    fields = ['nome', 'cpf', 'data_nascimento', 'matricula', 'escola', 'data_validade_cadastro', 'declaracao_escolar', 'status_aluno']
    success_url = reverse_lazy('aluno_list')
    success_message = "Dados do aluno atualizados com sucesso! ✅"

class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'educacional/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')

    # No DeleteView é um pouco diferente, precisamos sobrescrever o form_valid
    def form_valid(self, form):
        messages.success(self.request, "Aluno excluído do sistema! 🗑️")
        return super().form_valid(form)