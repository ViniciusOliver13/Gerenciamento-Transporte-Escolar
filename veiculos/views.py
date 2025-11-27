from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from .models import Veiculo

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculos/veiculo_list.html'
    context_object_name = 'veiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busca = self.request.GET.get('busca')
        if busca:
            queryset = queryset.filter(
                Q(placa__icontains=busca) | 
                Q(modelo__icontains=busca)
            )
        return queryset

class VeiculoCreateView(SuccessMessageMixin, CreateView):
    model = Veiculo
    template_name = 'veiculos/veiculo_form.html'
    fields = ['placa', 'modelo', 'ano', 'capacidade'] 
    success_url = reverse_lazy('veiculos:veiculo_list')
    success_message = "Veículo %(modelo)s cadastrado com sucesso! "

class VeiculoUpdateView(SuccessMessageMixin, UpdateView):
    model = Veiculo
    template_name = 'veiculos/veiculo_form.html'
    fields = ['placa', 'modelo', 'ano', 'capacidade']
    success_url = reverse_lazy('veiculos:veiculo_list')
    success_message = "Dados do veículo atualizados! "

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculos/veiculo_confirm_delete.html'
    success_url = reverse_lazy('veiculos:veiculo_list')

    def form_valid(self, form):
        messages.success(self.request, "Veículo removido da frota.")
        return super().form_valid(form)