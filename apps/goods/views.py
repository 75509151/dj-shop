from django.shortcuts import render
from .models import GoodsCategory
from rest_framework import viewsets, mixins
from .serializers import CategorySerializer

# Create your views here.


class CategoryView(viewsets.ModelViewSet):
# class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    paginator = None



