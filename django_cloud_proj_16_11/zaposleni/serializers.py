from rest_framework import serializers
from .models import Zaposleni


class ZaposleniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zaposleni
        fields = ['id', 'name', 'last_name', 'date_of_birth', 'salary']