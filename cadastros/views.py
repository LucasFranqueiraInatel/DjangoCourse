from django.shortcuts import render

from cadastros.models import Cidade


# Create your views here.

# function based views -> fbv
def lista_cidades(request):
    # ORM do Django
    qs = Cidade.objects.all()

    context = {
        "cidades": qs,
        "titulo":"SIDIA"
    }

    return render(request, 'cadastros/lista_cidades.html', context)

def detalhe_cidade(request):

    id_cidade = 3

    cidade = Cidade.objects.get(pk=id_cidade)
    # cidade = Cidade.objects.filter(nome='Belo Horizonte')
    print(cidade)

    context = {
        'cidades': cidade
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)