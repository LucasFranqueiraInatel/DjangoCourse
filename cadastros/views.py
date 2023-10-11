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
