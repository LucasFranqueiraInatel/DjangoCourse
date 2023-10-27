from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from cadastros.models import Cidade, Estado


class CidadeSerializer(ModelSerializer):
    estado_nome = serializers.ReadOnlyField(source='estado.nome')
    # estado = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all())

    class Meta:
        model = Cidade
        fields = ['id', 'estado_nome', 'estado', 'nome', 'capital', 'descricao']


class TestSerializer(Serializer):
    nome = serializers.CharField(max_length=45)
