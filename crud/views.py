from django.shortcuts import render
from django.http import Http404
from rest_framework import generics

from .models import Crudlist
from .serializers import CrudlistSerializer

class CrudList(generics.ListCreateAPIView):
    queryset = Crudlist.objects.all()
    serializer_class = CrudlistSerializer

class CrudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crudlist.objects.all()
    serializer_class = CrudlistSerializer

# http://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views
