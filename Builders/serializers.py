from dataclasses import field
from rest_framework import serializers
from .models import Builder


class BuilderSerializer(serializers.ModelSerializer):
    """
    1. This class is used to send a list of all the builder objects.
    2. It lists only the fields that are included in the fields list.
    """
    class Meta:
        model = Builder
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


# class CreateBuilderSerializer(serializers.ModelSerializer):
#     class Meta:
#         feilds = []
