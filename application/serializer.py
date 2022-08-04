from rest_framework import serializers
from .models import opensnz

# Serializers define the API representation.
class ser(serializers.ModelSerializer):
    class Meta:
        model = opensnz
        fields = ['id','temp','dt']