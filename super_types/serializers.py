from rest_framework import serializers
from .models import SuperTypes

class SupersTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperTypes
        fields = ['id', 'types']