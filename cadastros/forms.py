from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['nome']

        if nome == 'Itajuba':
            raise ValidationError({"nome": "Não podemos cadastras a cidade de Itajuba no sistema"})
            pass
