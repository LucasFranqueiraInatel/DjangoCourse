from django.urls import path

from cadastros.views import lista_cidades, detalhe_cidade

urlpatterns = [
    path('', lista_cidades, name='cidades-list'),
    path('detalhe/', detalhe_cidade, name='cidades-detalhe'),
]