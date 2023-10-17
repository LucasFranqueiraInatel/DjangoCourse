from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class SidiaBaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "PROJETO SIDIA"
        return context


class CidadeList(SidiaBaseListView):
    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):
    queryset = Cidade.objects.all()
    context_object_name = 'cidade'
    # pk_url_kwarg = 'id'
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):
    mode = Cidade
    # fields = ['nome', 'capital']
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    context_object_name = 'obj'
    success_message = "Cadastro Atualizado com Sucesso!"

