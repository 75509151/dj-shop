from django.shortcuts import render
from .models import GoodsCategory, Banner
from rest_framework import viewsets, mixins
from .serializers import CategorySerializer, BannerSerializer

# Create your views here.


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    paginator = None



class BannerView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    paginator = None

