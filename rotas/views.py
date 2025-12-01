from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views import View
from django.contrib import messages
from django.db.models import Count, Q
from django import forms
from .models import Rota
from educacional.models import Aluno
from veiculos.models import Veiculo
from usuarios.models import Motorista
from .models import Rota, ConfirmacaoViagem
from django.contrib.auth.decorators import login_required


# ============== LISTAGEM DE ROTAS ==============
class RotaListView(ListView):
    model = Rota
    template_name = 'rotas/rota_list.html'
    context_object_name = 'rotas'
    ordering = ['turno', 'nome']
    
    def get_queryset(self):
        # Adiciona contagem de alunos para cada rota
        return Rota.objects.annotate(
            total_alunos=Count('alunos')
        ).select_related('veiculo', 'motorista')


# ============== CRIAR ROTA ==============
class RotaCreateView(CreateView):
    model = Rota
    template_name = 'rotas/rota_form.html'
    fields = ['nome', 'turno', 'horario_inicio', 'prazo_limite_confirmacao', 'veiculo', 'motorista']
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adiciona widget HTML5 para TimeField
        form.fields['horario_inicio'].widget = forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
        )
        form.fields['prazo_limite_confirmacao'].widget = forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
        )
        return form
    
    def form_valid(self, form):
        # Salva o objeto primeiro
        self.object = form.save()
        # Adiciona mensagem de sucesso
        messages.success(self.request, f'✅ Rota "{self.object.nome}" criada com sucesso!')
        # Redireciona para a página de detalhes
        return redirect('rotas:rota_detail', pk=self.object.pk)


# ============== EDITAR ROTA ==============
class RotaUpdateView(UpdateView):
    model = Rota
    template_name = 'rotas/rota_form.html'
    fields = ['nome', 'turno', 'horario_inicio', 'prazo_limite_confirmacao', 'veiculo', 'motorista']
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Adiciona widget HTML5 para TimeField
        form.fields['horario_inicio'].widget = forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
        )
        form.fields['prazo_limite_confirmacao'].widget = forms.TimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
        )
        return form
    
    def get_success_url(self):
        messages.success(self.request, f' Rota "{self.object.nome}" atualizada!')
        return reverse_lazy('rotas:rota_detail', kwargs={'pk': self.object.pk})


# ============== DETALHES DA ROTA ==============
class RotaDetailView(DetailView):
    model = Rota
    template_name = 'rotas/rota_detail.html'
    context_object_name = 'rota'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rota = self.object
        
        # Alunos já alocados
        context['alunos'] = rota.alunos.all().order_by('nome')
        context['total_alunos'] = rota.alunos.count()
        
        # Capacidade do veículo
        if rota.veiculo:
            context['capacidade'] = rota.veiculo.capacidade
            context['vagas_disponiveis'] = rota.veiculo.capacidade - context['total_alunos']
            context['percentual_ocupacao'] = (context['total_alunos'] / rota.veiculo.capacidade * 100) if rota.veiculo.capacidade > 0 else 0
        else:
            context['capacidade'] = 0
            context['vagas_disponiveis'] = 0
            context['percentual_ocupacao'] = 0
        
        return context


# ============== ADICIONAR ALUNOS (MODAL/PÁGINA) ==============
class AdicionarAlunosView(View):
    template_name = 'rotas/adicionar_alunos.html'
    
    def get(self, request, pk):
        rota = get_object_or_404(Rota, pk=pk)
        
        # Filtros
        escola_filtro = request.GET.get('escola', '')
        bairro_filtro = request.GET.get('bairro', '')
        
        # Alunos disponíveis (não estão nesta rota e estão ATIVO)
        alunos_disponiveis = Aluno.objects.filter(
            status_aluno='ATIVO'
        ).exclude(
            id__in=rota.alunos.values_list('id', flat=True)
        )
        
        # Aplicar filtros
        if escola_filtro:
            alunos_disponiveis = alunos_disponiveis.filter(escola__icontains=escola_filtro)
        
        if bairro_filtro:
            alunos_disponiveis = alunos_disponiveis.filter(endereco__icontains=bairro_filtro)
        
        alunos_disponiveis = alunos_disponiveis.order_by('escola', 'nome')
        
        # Lista de escolas para os filtros
        escolas = Aluno.objects.filter(status_aluno='ATIVO').values_list('escola', flat=True).distinct().order_by('escola')
        
        context = {
            'rota': rota,
            'alunos_disponiveis': alunos_disponiveis,
            'escolas': escolas,
            'escola_filtro': escola_filtro,
            'bairro_filtro': bairro_filtro,
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        rota = get_object_or_404(Rota, pk=pk)
        
        # Recebe os IDs dos alunos selecionados
        alunos_ids = request.POST.getlist('alunos_selecionados')
        
        if not alunos_ids:
            messages.warning(request, '⚠️ Nenhum aluno foi selecionado.')
            return redirect('rotas:adicionar_alunos', pk=pk)
        
        # Verifica capacidade do veículo
        if rota.veiculo:
            vagas_disponiveis = rota.veiculo.capacidade - rota.alunos.count()
            
            if len(alunos_ids) > vagas_disponiveis:
                messages.error(
                    request, 
                    f'❌ Capacidade excedida! Veículo tem apenas {vagas_disponiveis} vaga(s) disponível(is).'
                )
                return redirect('rotas:adicionar_alunos', pk=pk)
        
        # Adiciona os alunos à rota
        alunos = Aluno.objects.filter(id__in=alunos_ids)
        rota.alunos.add(*alunos)
        
        messages.success(
            request, 
            f'✅ {len(alunos_ids)} aluno(s) adicionado(s) à rota "{rota.nome}"!'
        )
        
        return redirect('rotas:rota_detail', pk=pk)


# ============== REMOVER ALUNO DA ROTA ==============
def remover_aluno_rota(request, pk, aluno_id):
    rota = get_object_or_404(Rota, pk=pk)
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    
    if request.method == 'POST':
        rota.alunos.remove(aluno)
        messages.success(request, f'✅ Aluno "{aluno.nome}" removido da rota.')
    
    return redirect('rotas:rota_detail', pk=pk)


# ============== DELETAR ROTA ==============
class RotaDeleteView(DeleteView):
    model = Rota
    template_name = 'rotas/rota_confirm_delete.html'
    success_url = reverse_lazy('rotas:rota_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '✅ Rota deletada com sucesso!')
        return super().delete(request, *args, **kwargs)


@login_required
def confirmar_viagem(request, rota_id, tipo):
    aluno = getattr(request.user, 'aluno_profile', None)
    if aluno is None:
        messages.error(request, 'Somente alunos podem confirmar viagens.')
        return redirect('usuarios:home')

    rota = get_object_or_404(Rota, id=rota_id)
    data_viagem = date.today()

    if tipo not in ['IDA', 'VOLTA']:
        messages.error(request, 'Tipo de viagem inválido.')
        return redirect('educacional:painel_aluno')

    confirmacao, criada = ConfirmacaoViagem.objects.get_or_create(
        aluno=aluno,
        rota=rota,
        data_viagem=data_viagem,
        tipo=tipo,
    )

    if criada:
        messages.success(
            request,
            f'Viagem de {tipo.lower()} confirmada hoje na rota "{rota.nome}".'
        )
    else:
        messages.info(
            request,
            f'Você já tinha confirmado a {tipo.lower()} de hoje na rota "{rota.nome}".'
        )

    return redirect('educacional:painel_aluno')
