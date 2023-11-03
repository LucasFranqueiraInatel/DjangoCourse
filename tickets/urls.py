from django.contrib.auth.decorators import login_required
from django.urls import include, path

from tickets.views import NovaSolicitacao

urlpatterns = [
    path('tickets/', NovaSolicitacao.as_view(), name='nova-solicitacao-ticket')
]