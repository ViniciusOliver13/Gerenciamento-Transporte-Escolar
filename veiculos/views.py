from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Veiculo
from usuarios.models import Motorista


VEICULO_LIST_URL = reverse_lazy('veiculos:veiculo_list') 

class VeiculoListView(ListView):
    """ Exibe a lista de todos os veículos cadastrados. """
    model = Veiculo
    template_name = 'veiculos/veiculo_list.html'
    context_object_name = 'veiculos' 

class VeiculoCreateView(CreateView):
    """ Permite ao Gestor cadastrar um novo veículo. """
    model = Veiculo
    
    fields = ['placa', 'modelo', 'capacidade', 'motorista'] 
    template_name = 'veiculos/veiculo_form.html' 
    success_url = VEICULO_LIST_URL

class VeiculoUpdateView(UpdateView):
    """ Permite ao Gestor editar um veículo existente. """
    model = Veiculo
    fields = ['placa', 'modelo', 'capacidade', 'motorista']
    template_name = 'veiculos/veiculos_form.html'
    success_url = VEICULO_LIST_URL

class VeiculoDeleteView(DeleteView):
    """ Permite ao Gestor remover um veículo. """
    model = Veiculo
    template_name = 'veiculos/veiculo_confirm_delete.html'
    success_url = VEICULO_LIST_URL