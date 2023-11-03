from django.shortcuts import render
from django.views import View

from tickets.forms import NovaSolicitacaoForm


class NovaSolicitacao(View):

    def get(self, request):

        form = NovaSolicitacaoForm

        return render(request, 'tickets/form.html', {'form': form})

    # def post(self, request):
    #
    #     form = NovaSolicitacaoForm(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #
    #         obj = form.save(commit=True)
    #         obj.save()
    #
    #         interacao = Interacao.objects.create(solicitacao=obj, tipo=Interacao.TIPO_STATUS_CHANGE, descricao='Solicitação aberta')
    #         interacao.send_mail_message()
    #
    #         return redirect('cidades-list')
    #
    #     return render(request, 'tickets/form.html', {'form': form})