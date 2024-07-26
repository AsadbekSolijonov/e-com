from django.shortcuts import render
from rest_framework import viewsets

from shop.models import Category
from shop.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
