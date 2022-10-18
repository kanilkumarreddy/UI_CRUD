from rest_framework import serializers 
from.models import Bank_Customer
from dataclasses import fields

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank_Customer
        fields=("__all__")