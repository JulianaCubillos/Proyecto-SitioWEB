from django.db.models import fields
from rest_framework import serializers
from maquinadb.models import Maquina

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'