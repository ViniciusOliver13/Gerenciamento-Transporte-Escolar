from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
        except:
            context['nome_exibicao'] = user.username
            
        return context