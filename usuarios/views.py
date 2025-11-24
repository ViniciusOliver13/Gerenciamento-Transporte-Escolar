from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from rotas.models import Rota

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
        # Tentativa 1: Aluno tem rotas
        if hasattr(aluno, 'rotas'):
            rotas = aluno.rotas.all()
        else:
            rotas = Rota.objects.filter(alunos=aluno)
    return render(request, 'educacional/painel_aluno.html', {'aluno': aluno, 'rotas': rotas})


@login_required
def painel_motorista(request):
    motorista = getattr(request.user, 'motorista_profile', None)
    if motorista is not None:
        # Ajuste conforme o relacionamento, supondo ManyToMany
        rotas = Rota.objects.filter(motorista=motorista)
    else:
        rotas = []
    return render(request, 'usuarios/painel_motorista.html', {'motorista': motorista, 'rotas': rotas})



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
