from django.shortcuts import render
from models import Builder
from serializers import BuilderSerializer
from rest_framework import viewsets



# Create your views here.
class BuilderViewSet(viewsets.ModelViewSet):
    queryset = Builder.objects.all()
    serializer_class = BuilderSerializer    