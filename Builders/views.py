from rest_framework import generics

from Builders.serializers import BuilderSerializer
from .models import Builder


class Builders(generics.ListAPIView):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer
