from django.shortcuts import render, get_object_or_404

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

def detalhe_cidade(request, id):

    # id_cidade = request.GET['id_cidade']


    cidade = get_object_or_404(Cidade, pk=id)
    # cidade = Cidade.objects.get(pk=id_cidade)
    # cidade = Cidade.objects.filter(nome='Belo Horizonte')

    context = {
        'cidade': cidade
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)