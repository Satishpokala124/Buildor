from dataclasses import field
from rest_framework import serializers
from models import Builder
class BuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Builder
        field = '__all__'