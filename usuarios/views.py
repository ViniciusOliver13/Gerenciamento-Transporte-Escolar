from collections import defaultdict
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from .models import Motorista
from datetime import date
hoje = date.today()

from rotas.models import ConfirmacaoViagem, Rota

@login_required
def redirect_usuario(request):
    user = request.user
    if hasattr(user, 'gestor_profile'):
        return redirect('usuarios:home')
    elif hasattr(user, 'motorista_profile'):
        return redirect('usuarios:painel_motorista')
    elif hasattr(user, 'aluno_profile'):
        return redirect('educacional:painel_aluno')
    else:
        return redirect('usuarios:home')


@login_required
def painel_aluno(request):
    aluno = getattr(request.user, 'aluno_profile', None)
    if aluno is None:
        rotas = []
    else:
        if hasattr(aluno, 'rotas'):
            rotas = aluno.rotas.all()
        else:
            rotas = Rota.objects.filter(alunos=aluno)
    return render(request, 'educacional/painel_aluno.html', {'aluno': aluno, 'rotas': rotas})


@login_required
def painel_motorista(request):
    motorista = getattr(request.user, 'motorista_profile', None)
    if motorista is None:
        return redirect('usuarios:home')

    rotas = Rota.objects.filter(motorista=motorista).select_related('veiculo').prefetch_related('alunos')
    hoje = date.today()

    # {rota_id: {aluno_id: set(['IDA','VOLTA'])}}
    confirmacoes = {}
    qs = ConfirmacaoViagem.objects.filter(rota__in=rotas, data_viagem=hoje)
    for c in qs:
        confirmacoes.setdefault(c.rota_id, {})
        confirmacoes[c.rota_id].setdefault(c.aluno_id, set())
        confirmacoes[c.rota_id][c.aluno_id].add(c.tipo)

    # total (ida+volta) por rota
    confirma_por_rota = {}
    for rota_id, alunos_dict in confirmacoes.items():
        total = 0
        for tipos in alunos_dict.values():
            total += len(tipos)
        confirma_por_rota[rota_id] = total

    context = {
        'motorista': motorista,
        'rotas': rotas,
        'confirmacoes': confirmacoes,
        'confirma_por_rota': confirma_por_rota,
        'hoje': hoje,
    }
    return render(request, 'usuarios/painel_motorista.html', context)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        try:
            if hasattr(user, 'gestor_profile'):
                context['nome_exibicao'] = user.gestor_profile.nome
            elif hasattr(user, 'motorista_profile'):
                context['nome_exibicao'] = user.motorista_profile.nome
            else:
                context['nome_exibicao'] = user.username
        except Exception:
            context['nome_exibicao'] = user.username
            
        return context


class MotoristaListView(ListView):
    model = Motorista
    template_name = 'usuarios/motorista_list.html'
    context_object_name = 'motoristas'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca')
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) | 
                Q(cnh__icontains=busca) |
                Q(cpf__icontains=busca)
            )
        return queryset

class MotoristaCreateView(SuccessMessageMixin, CreateView):
    model = Motorista
    template_name = 'usuarios/motorista_form.html'
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco', 'telefone', 'cnh', 'data_validade_cnh']
    success_url = reverse_lazy('usuarios:motorista_list')
    success_message = "Motorista %(nome)s cadastrado com sucesso! "

class MotoristaUpdateView(SuccessMessageMixin, UpdateView):
    model = Motorista
    template_name = 'usuarios/motorista_form.html'
    fields = ['nome', 'cpf', 'data_nascimento', 'endereco', 'telefone', 'cnh', 'data_validade_cnh']
    success_url = reverse_lazy('usuarios:motorista_list')
    success_message = "Dados do motorista atualizados! "

class MotoristaDeleteView(DeleteView):
    model = Motorista
    template_name = 'usuarios/motorista_confirm_delete.html'
    success_url = reverse_lazy('usuarios:motorista_list')

    def form_valid(self, form):
        messages.success(self.request, "Motorista removido da equipe.")
        return super().form_valid(form)